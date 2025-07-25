import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

# === STEP 1: Load the data ===
print("Loading train and test datasets...")
train_path = os.path.join(".", "raw-data", "train.csv")
test_path = os.path.join(".", "raw-data", "test.csv")

train = pd.read_csv(train_path)
test = pd.read_csv(test_path)
print(f"Train data shape: {train.shape}, Test data shape: {test.shape}")

# === STEP 2: Prepare target and features ===
print("Preparing target (SalePrice) and feature columns...")
y = np.log1p(train["SalePrice"])
X = train.drop(columns=["SalePrice", "Id"])
X_test = test.drop(columns=["Id"])

# Identify numeric and categorical columns
num_cols = X.select_dtypes(include=["int64", "float64"]).columns
cat_cols = X.select_dtypes(include=["object"]).columns
print(f"Numeric features: {len(num_cols)}, Categorical features: {len(cat_cols)}")

# === STEP 3: Preprocessing pipeline ===
numeric_transformer = SimpleImputer(strategy="median")
categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, num_cols),
        ("cat", categorical_transformer, cat_cols)
    ]
)

# === STEP 4: Train-Test split ===
print("Splitting data into training and validation sets...")
X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# === STEP 5: Model building ===
print("Building Ridge Regression model...")
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", Ridge(alpha=5.0))
])

# === STEP 6: Training and validation ===
print("Training the model on training set...")
model.fit(X_train, y_train)
y_pred = model.predict(X_valid)

rmse = mean_squared_error(y_valid, y_pred, squared=False)
print(f"Validation RMSE (log1p target): {rmse:.4f}")

# === STEP 7: Final training on full dataset and test prediction ===
print("Retraining on the full training dataset and predicting test set...")
model.fit(X, y)
preds = np.expm1(model.predict(X_test))

# === STEP 8: Create submissions directory ===
submissions_dir = os.path.join(os.path.dirname(__file__), "submissions")
os.makedirs(submissions_dir, exist_ok=True)

# Save Kaggle submission
submission_path = os.path.join(submissions_dir, "house_price_ridge.csv")
submission = pd.DataFrame({"Id": test["Id"], "SalePrice": preds})
submission.to_csv(submission_path, index=False)
print(f"\nSubmission saved to: {submission_path}")

# === STEP 9: Preview predictions with house specifications ===
print("\n=== Prediction Preview ===")
display_cols = ['Id', 'MSZoning', 'Neighborhood', 'OverallQual', 'GrLivArea', 'GarageCars']
preview = test[display_cols].copy()
preview['PredictedPrice'] = preds
print(preview.head(10))

# Save preview with house specifications and predictions
preview_path = os.path.join(submissions_dir, "predicted_house_details.csv")
preview.to_csv(preview_path, index=False)
print(f"Preview of predicted house details saved to: {preview_path}")

# === STEP 10: Correlation Heatmap ===
print("\nGenerating correlation heatmap...")
corr = train.corr(numeric_only=True)
plt.figure(figsize=(12, 8))
sns.heatmap(corr, cmap='coolwarm', annot=False)
plt.title('Correlation Heatmap of Numeric Features')
heatmap_path = os.path.join(submissions_dir, "correlation_heatmap.png")
plt.savefig(heatmap_path)
plt.close()
print(f"Correlation heatmap saved to: {heatmap_path}")

# === STEP 11: Top numeric features ===
print("\n=== Top Numeric Features Influencing Price ===")
ridge_model = model.named_steps['regressor']
feature_names = list(num_cols)
coefficients = ridge_model.coef_[:len(feature_names)]
coef_df = pd.DataFrame({'Feature': feature_names, 'Coefficient': coefficients})
coef_df = coef_df.reindex(coef_df.Coefficient.abs().sort_values(ascending=False).index)
print(coef_df.head(10))

# Save top features
top_features_path = os.path.join(submissions_dir, "top_features.csv")
coef_df.to_csv(top_features_path, index=False)
print(f"Top feature coefficients saved to: {top_features_path}")

print("\nThe model predicts house prices based on patterns in numeric features "
      "like OverallQual, GrLivArea, TotalBsmtSF, etc., and categorical variables "
      "such as Neighborhood and MSZoning. Ridge regression assigns weights "
      "(coefficients) to each feature based on its influence on SalePrice.")
