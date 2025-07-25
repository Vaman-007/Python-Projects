import os
import cv2
from deepface import DeepFace

# -------- settings ----------
MODEL_NAME = "Facenet"          # Fast & accurate enough
DETECTOR_BACKEND = "opencv"     # Light detector
ENFORCE_DETECTION = False       # Avoid hard errors if face not perfectly detected
REGISTER_DIR = "user_faces"
CAM_INDEX = 0                   # Try 0, if black screen try 1 or 2
USE_CAP_DSHOW = True            # On Windows, helps with stuck camera
# ----------------------------

os.makedirs(REGISTER_DIR, exist_ok=True)

def open_camera(index=0):
    # On Windows, CAP_DSHOW avoids long delay or stuck capture
    if USE_CAP_DSHOW and hasattr(cv2, "CAP_DSHOW"):
        cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
    else:
        cap = cv2.VideoCapture(index)
    return cap

def capture_photo(filename="captured.jpg", win_name="Capture Photo"):
    cap = open_camera(CAM_INDEX)
    if not cap.isOpened():
        raise RuntimeError("Cannot open camera. Try a different CAM_INDEX, close other apps, "
                           "or run Python from a normal terminal (not WSL / remote session).")

    print("Press SPACE to capture, or ESC to cancel.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame from camera.")
            continue

        cv2.imshow(win_name, frame)
        key = cv2.waitKey(1) & 0xFF

        if key == 27:  # ESC
            filename = None
            break
        elif key == 32:  # SPACE
            cv2.imwrite(filename, frame)
            print(f"Saved: {filename}")
            break

    cap.release()
    cv2.destroyAllWindows()
    return filename

def register_user():
    name = input("Enter your name to register: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    out_path = os.path.join(REGISTER_DIR, f"{name}.jpg")
    print(f"Capturing face for {name}...")
    photo = capture_photo(out_path, win_name=f"Register - {name}")
    if photo is None:
        print("Registration cancelled.")
        return

    print(f"✅ Face registered as {name}")

def login_user():
    reg_users = [f for f in os.listdir(REGISTER_DIR)
                 if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    if not reg_users:
        print("No registered users found. Please register first.")
        return

    print("Capturing login photo...")
    login_path = "login.jpg"
    photo = capture_photo(login_path, win_name="Login")
    if photo is None:
        print("Login cancelled.")
        return

    matched = False
    for reg_user in reg_users:
        reg_path = os.path.join(REGISTER_DIR, reg_user)
        try:
            result = DeepFace.verify(
                img1_path=login_path,
                img2_path=reg_path,
                enforce_detection=ENFORCE_DETECTION,
                model_name=MODEL_NAME,
                detector_backend=DETECTOR_BACKEND
            )
        except Exception as e:
            print(f"DeepFace error for {reg_user}: {e}")
            continue

        if result.get("verified"):
            person = os.path.splitext(reg_user)[0]
            print(f"✅ Login successful! Welcome, {person} 🎉")
            matched = True
            break

    if not matched:
        print("❌ Face not recognized. Access denied.")

def main():
    while True:
        print("\n--- Face Auth ---")
        print("1) Register")
        print("2) Login")
        print("3) Quit")
        choice = input("Choose (1/2/3): ").strip()
        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
