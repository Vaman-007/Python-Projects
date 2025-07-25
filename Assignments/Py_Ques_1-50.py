# Questions for Python Programming Assignments

#   1.	Write a Python program to find the largest of three numbers.
# 	2.	Create a program that checks whether a number is even or odd.
# 	3.	Accept a string from the user and reverse it.
# 	4.	Write a program to count the number of vowels in a string.
# 	5.	Create a calculator using if-else (add, subtract, multiply, divide).
# 	6.	Write a program to check if a number is prime.
# 	7.	Display the multiplication table of a given number.
# 	8.	Write a program to print the Fibonacci series up to n terms.
# 	9.	Write a program to find the factorial of a number using a loop.
# 	10.	Accept a number and check whether it is a palindrome.
# 	11.	Find the sum of digits of a number using a while loop.
# 	12.	Create a program to convert Celsius to Fahrenheit.
# 	13.	Write a Python function to find the maximum of two numbers.
# 	14.	Accept a list of numbers and return the average.
# 	15.	Find the second largest number in a list.
# 	16.	Accept a sentence and count the number of words.
# 	17.	Accept a list and remove all duplicates from it.
# 	18.	Write a program to create a dictionary from two lists.
# 	19.	Accept a list and sort it without using sort() function.
# 	20.	Write a function that checks if a string is a pangram.
# 	21.	Write a function to check if the input is a number or not.
# 	22.	Accept a string and check if it is an anagram of another.
# 	23.	Accept a number and print its binary, octal, and hexadecimal.
# 	24.	Accept a list and print all elements greater than 50.
# 	25.	Write a function to count uppercase and lowercase letters in a string.
#   26.	Write a Python program using a lambda function to square all elements in a list.
#   27.	Create a function that returns a list of prime numbers from 1 to 100.
#   28.	Write a program to implement a simple calculator using functions.
#   29.	Implement a recursive function to compute factorial.
#   30.	Create a Python program using OOP for student management (class, object, init).
#   31.	Write a program to read a file and count the number of lines and words.
#   32.	Write a Python decorator to print the execution time of a function.
#   33.	Create a class BankAccount with deposit and withdraw methods.
#   34.	Implement a generator to yield even numbers from 1 to n.
#   35.	Write a function using *args and **kwargs to print any number of arguments.
#   36.	Use list comprehension to create a list of squares of even numbers from 1 to 20.
#   37.	Create a function that takes a list and returns only unique elements.
#   38.	Write a Python program to merge two dictionaries.
#   39.	Create a class that inherits from another class and overrides a method.
#   40.	Write a function to find common elements between two lists.
#   41.	Implement a program to demonstrate try-except-finally for exception handling.
#   42.	Write a program to parse and display JSON data from a string.
#   43.	Create a class that demonstrates the use of private and protected members.
#   44.	Write a Python function to check if a string is a valid email address.
#   45.	Accept a CSV file and convert it into a list of dictionaries.
#   46.	Create a simple login system using dictionary and input.
#   47.	Write a function to flatten a nested list using recursion.
#   48.	Demonstrate use of map(), filter(), and reduce() on a list.
#   49.	Build a small CLI app that takes user input and performs basic operations.
#   50.	Create a mini Python quiz that takes answers from the user and displays score.


#   1.	Write a Python program to find the largest of three numbers.
print('*'*30)
print("Enter 3 numbers:")
num1 = int(input("Enter 1st Number:"))
num2 = int(input("Enter 2nd Number:"))
num3 = int(input("Enter 3rd Number:"))

print("Numbers Entered: ",num1,num2,num3)
if num1 > num2:
    if num1 > num3:
        print(num1,"is the largest number")
    else:
        print(num3,"is the largest number")
else:
    if num2 > num3:
        print(num2,"is the largest number")
    else:
        print(num3,"is the largest number")

print('*'*30)

# 	2.	Create a program that checks whether a number is even or odd.
print('*'*30)
number = int(input("Enter a number to check either the number is even or odd: "))
print("Entered Number: ",number)
if number%2:
    print(number,"is Odd")
else:
    print(number,"is Even")
print('*'*30)

# 	3.	Accept a string from the user and reverse it.
print('*'*30)
string = input("Enter a String to check it's reverse: ")
rev = string[::-1]
print(f"Reverse of \n\"{string}\" is : {rev}")
print('*'*30)

# 	4.	Write a program to count the number of vowels in a string.
print('*'*30)
count = 0
string = input("Enter a String to count it's vowels: ")
for i in string:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count += 1
print(f"There are {count} vowels in {string}")
print('*'*30)

# 	5.	Create a calculator using if-else (add, subtract, multiply, divide).

print('*'*30)
while True:
    expression = input("Enter a Task to Perform eg:(10 + 20)\n")
    if expression != 'exit':
        [n1,e,n2] = expression.split(' ')

        if expression:    
            if e == '+':
                print(expression,'=',int(n1)+int(n2))
            elif e == '-':
                print(expression,'=',int(n1)-int(n2))
            elif e == '*':
                print(expression,'=',int(n1)*int(n2))
            elif e == '/':
                print(expression,'=',int(n1)/int(n2))
    
    else:
        break
print('*'*30)

# 	6.	Write a program to check if a number is prime.
print('*'*30)
n = int(input("Enter a number to check whether it is Prime or Not"))
def checkPrime(num):
    i = 2
    while i < num:
        if num%i == 0:
            print(f'{num} is not prime')
            return
        i+=1
    print(f"{num} is prime")
    return
checkPrime(n)
print('*'*30)

# 	7.	Display the multiplication table of a given number.
print('*'*30)
n = int(input("Enter a number print it's table"))
for i in range(1,11):
    print(f"{n} * {i} = {i*n}")

print('*'*30)

# 	8.	Write a program to print the Fibonacci series up to n terms.
def fabo(iterate,n=0,m=1,current=1):
    if current <= iterate:
        if current == 1:
            print("0 ",end="")
            fabo(iterate,n,m,current+1)
        elif current == 2:
            print("1 ",end="")
            fabo(iterate,n,m,current+1)
        else:
            print(f"{n+m} ",end="")
            fabo(iterate,m,n+m,current+1)
    return
print('*'*30)
iterations = int(input("Enter n to print the Fibonacci series up to n terms"))
print(f"Fabonacci Series up to {iterations} terms:")
fabo(iterations)
print()
print('*'*30)

# 	9.	Write a program to find the factorial of a number using a loop.
print('*'*30)
number = int(input("Enter a number to find it's factorial"))
factorial = 1
for i in range(1,number+1):
    factorial*=i
print(f"Factorial of {number} is {factorial}")
print('*'*30)

# 	10.	Accept a number and check whether it is a palindrome.
print('*'*30)
num = int(input("Enter a number to check whether it is palendrome or not"))
numstr=str(num)
if numstr == numstr[::-1]:
    print(f"{numstr} is a palendrome")
else:
    print(f"{numstr} is not a palendrome")
print('*'*30)

# 	11.	Find the sum of digits of a number using a while loop.
print('*'*30)
num = int(input("Enter a number to Find the sum of digits of a number"))
numstr=str(num)
total = 0
for i in numstr:
    total+=int(i)
print(f"The sum of digits of {num} is {total}")
print('*'*30)

# 	12.	Create a program to convert Celsius to Fahrenheit.
print('*'*30)
c = float(input("Enter the temprature in Celsius"))
print(f"{c}°C = {(c * 9/5) + 32}°F")
print('*'*30)

# 	13.	Write a Python function to find the maximum of two numbers.
num1,num2 = input("Enter 2 numbers seperated by ' '").split(' ')
num1,num2 = int(num1),int(num2)
if num1>num2:
    print(f"{num1} is greater than {num2}")
elif num2>num1:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num2} is equal to {num1}")

# 	14.	Accept a list of numbers and return the average.
print('*'*30)
numbers = input("Enter a list of numbers seperated by ',' to find their average")
nums = []
for i in numbers.split(','):
    nums.append(int(i))
total = 0
for i in nums:
    total += i
print(f"Average of {nums} = {total/len(nums)}")
print('*'*30)

# 	15.	Find the second largest number in a list.
print('*'*30)
numbers = input("Enter a list of numbers to find second largest number")
nums = numbers.split(',')
nums = [int(num) for num in nums]
top = 0
stop = 0
for i in nums:
    if i>top:
        top = i
for i in nums:
    if i>stop and i<top:
        stop = i
print(f"{stop} is the second largest element in {nums}")
print('*'*30)

# 	16.	Accept a sentence and count the number of words.
print('*'*30)
sentensein = input("Enter a sentence to find the number of words")
sentense=sentensein
a=[',','.']
for i in a:
    sentense = sentense.replace(i,"")
words=len(sentense.split())
print(f"There are {words} words in \n{sentensein}")
print('*'*30)

# 	17.	Accept a list and remove all duplicates from it.
print('*'*30)
items = input("Enter elements seperated by ','")
items = list(items.split(','))
print("List : ",items)
uniqueItems = []
for i in items:
    if i not in uniqueItems:
        uniqueItems.append(i)
print(f"List after removing duplicates : {uniqueItems}")
print('*'*30)

# 	18.	Write a program to create a dictionary from two lists.
print('*'*30)
list1 = input("Enter the names for the values seperate by ','")
list2 = input("Enter the values for the names seperate by ','")
list1 = list1.split(',')
list2 = list2.split(',')
dect = {}
if len(list1) == len(list2):
    length = len(list1)
    for i in range(length):
        if list1[i] in dect:
            dect[list1[i]].append(list2[i])
        else:
            dect[list1[i]] = [list2[i]]
else:
    print("there are not sufficient names or values there should be equal names and values")
print(dect)
print('*'*30)

# 	19.	Accept a list and sort it without using sort() function.
print('*'*30)
items = input("Enter elements seperated by ','")
items = items.split(',')
n = len(items)
for i in range(n):
    for j in range(n-i-1):
        if items[j]>items[j+1]:
            items[j],items[j+1]=items[j+1],items[j]
print(items)
print('*'*30)

# 	20.	Write a function that checks if a string is a pangram.
print('*'*30)
letters = 'abcdefghijklmnopqrstuvwxyz'
sentensein = input("Enter a string to check if it is pangram or not")
def checkPang(sentense):
    for i in letters:
        if i not in sentense.lower():
            print(f"String \"{sentense}\" is not pangram")
            return
    print(f"String \"{sentense}\" is pangram")
    return
checkPang(sentensein)
print('*'*30)

# 	21.	Write a function to check if the input is a number or not.
print('*'*30)
strg = input("Enter a string to check if it is number or not")
try:
       int(strg)
       print(f"{strg} is a number")
except ValueError:
       print(f"{strg} is not a number")

print('*'*30)

# 	22.	Accept a string and check if it is an anagram of another.
print('*'*30)
strg = "Halu"
strg2 = "Halu"
strg.index(strg2)
print('*'*30)

# 	23.	Accept a number and print its binary, octal, and hexadecimal.
print('*'*30)
number = int(input("Enter a number to find it's Binary, Octal and HexaDecimal: "))
def binary(num):
    bdat=[]
    while num!=0:
        i = 0
        while num >= 2**i:
            i+=1
        num = num-2**(i-1)
        bdat.append(i-1)
    rng=max(bdat)
    for j in range(rng,-1,-1):
        if j in bdat:
            print(1,end="")
        else:
            print(0,end="")
    print()
        
def octal(num):
    odat = []
    while num > 0:
        odat.insert(0,num%8)
        num //= 8
    for i in odat:
        if (odat.index(i)+1)%4==0:
            print(" ",end="")
        print(i,end="")
    print()
        
def getVal(a):
    vals={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    if a > 9:
        return vals.get(a)
    else:
        return a
def hexDec(num):
    hddat = []
    while num > 0:
        hddat.insert(0,getVal(num%16))

        num //= 16
    for i in hddat:
        print(i,end="")
    print()
print("Binary:")
binary(number)
print("Octal:")
octal(number)
print("Hexa Decimal:")
hexDec(number)
print('*'*30)

# 	24.	Accept a list and print all elements greater than 50.
print('*'*30)


print('*'*30)

# 	25.	Write a function to count uppercase and lowercase letters in a string.
print('*'*30)
letters = "abcdefghijklmnopqrstuvwxyz"
strng = input("Enter a String")
a,b = 0,0
for i in strng:
    if i in letters:
        a+=1
    elif i in letters.upper():
        b+=1
print(f"There are {a} lower case letters and {b} upper case letters in {strng}")
print('*'*30)

# 26.	Write a Python program using a lambda function to square all elements in a list.
print('*'*30)
sqr = lambda x: x * x
l1 = input("Enter the numbers seperated by ','")
l1 = l1.split(',')
l1 = list(map(int,l1))

print(l1)
l1 = list(map(sqr,l1))
print(l1)
print('*'*30)

#	27.	Create a function that returns a list of prime numbers from 1 to 100.
print('*'*30)
def checkPrime(num):
    i = 2
    while i < num:
        if num%i == 0:
            return
        i+=1
    print(f"{num} ",end="")
    return
for i in range(1,101):
    checkPrime(i)
print()
print('*'*30)

#	28.	Write a program to implement a simple calculator using functions.

print('*'*30)
print("\t\tCalculator\n\n")
choice = 'y'
while choice == 'y':
    print('*'*30)
    num1 = int(input("Enter First Number:"))
    print("Enter your task to perform (+,-,*,/,'0 to exit'):")
    option = input("Enter your choice(+,-,*,/)")
    num2 = int(input("Enter Second Number:"))
    list = ['+','-','*','/','0']
    if option in list:
        match option:
            case '+':
                choice = 'y'
                print(num1,option,num2,"=",num1 + num2)
            case '-':
                choice = 'y'
                print(num1,option,num2,"=",num1 - num2)
            case '*':
                choice = 'y'
                print(num1,option,num2,"=",num1 * num2)
            case '/':
                choice = 'y'
                if num2 != 0: 
                    print(num1,option,num2,"=",num1 / num2)
                else:
                    print("Denominator Can't Be 0")            
    else:
        print("Invalid Choice retry")
    print('*'*30)
    choice = input("Continue? (y,n)")

#	29.	Implement a recursive function to compute factorial.
print('*'*30)
def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)
print("factorial of the number is",factorial(int(input("Enter a number to find it's factorial"))))
print('*'*30)

#	30.	Create a Python program using OOP for student management (class, object, init).
print('*'*30)

class Student:
    def __init__(self,ssid,name,age,phoneNo):
        self.ssid=ssid
        self.name=name
        self.age=age
        self.phoneNo=phoneNo
    def showDetails(self):
        print(f"""           
Student Details:
            ssid:{self.ssid}
            Name:{self.name}
            Age:{self.age}
            phoneNo:{self.phoneNo}
        """)
students = []

students.append(Student(1, "Pavneet", 18, 9818932172))
students.append(Student(2, "Aman", 19, 9876543210))
students.append(Student(3, "Simran", 17, 9123456789))

for student in students:
    student.showDetails()
print('*'*30)

#	31.	Write a program to read a file and count the number of lines and words.
print('*'*30)
f = open("./50Ques/Q31.txt","r")
word=1
line=1
for i in f.read():
    if i == "\n":
        line+=1
        word+=1
    if i == " ":
        word+=1
print(f"There are {word} words and {line} lines")
print('*'*30)

#	32.	Write a Python decorator to print the execution time of a function.
print('*'*30)
import time
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Time taken to execute : {end - start:.4f}")
    return wrapper

@timer
def myFn():
    for i in range(2000000):
        pass

myFn()
print('*'*30)

#	33.	Create a class BankAccount with deposit and withdraw methods.
print('*'*30)
def atmMachine():
    balance = 0.0
    def withdraw():
        nonlocal balance
        balance = balance - int(input("Enter amount to withdraw"))
        print(f"your new balance is : {balance:.2f}")
    def deposit():
        nonlocal balance
        balance = balance + int(input("Enter amount to deposit"))
        print(f"your new balance is : {balance:.2f}")
    def display():
        print(f"your balance is : {balance:.2f}")
    print("\t\t\tWelcome to Gareeb Khana")

    if input("Enter Card") == "card" and input("Enter Pin") == "1234":
        while True:
            choice = int(input("Enter the task to perform \n\t1. Withdraw\n\t2. Deposit\n\t3. Show Balance\n\t0. Exit\n\t"))
            match choice:
                case 1:
                    withdraw()
                case 2:
                    deposit()
                case 3:
                    display()
                case 0:
                    break
                case _:
                    print("Invalid Choice")
    else:
        print("Invalid Card Credentials")
atmMachine()
print('*'*30)

#	34.	Implement a generator to yield even numbers from 1 to n.
print('*'*30)
number = int(input("Enter a number"))
def numbers(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            yield i

for i in numbers(number):
    print(i,end=" ")

print()
print('*'*30)

#	35.	Write a function using *args and **kwargs to print any number of arguments.

def print_arguments(*args, **kwargs):
    print("Positional arguments (*args):")
    for arg in args:
        print(arg)
    
    print("\nKeyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_arguments(1, 2, 3, name="Pavneet", age=21, city="Delhi")

# 36. Use list comprehension to create a list of squares of even numbers from 1 to 20.
squares_of_evens = [x**2 for x in range(1, 21) if x % 2 == 0]
squares_of_evens

# 37. Function to return unique elements
def get_unique_elements(input_list):
    unique = []
    for element in input_list:
        if element not in unique:
            unique.append(element)
    return [unique]

get_unique_elements([3, 5, 2, 5, 3, 7, 8, 2])

# 38. Dictionary merging function

def merge_dictionaries(*dicts):
    merged = {}
    for d in dicts:
        merged.update(d)
    return merged

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'a': 10}  
merge_dictionaries(dict1, dict2, dict3)

# 39. Class inheritance with method overriding
class Animal:
    def __init__(self, animal):
        self.animal = animal
    
    def eat(self):
        return f" is eating"

class Dawg(Animal):
    def __init__(self, animal):
        super().__init__(animal)
        self.animal = animal
    
    def eat(self): 
        return f"{self.animal}{super().eat()}"

# Example usage
dawg = Dawg("dawg")
dawg.eat()

# 40. Common elements finder
def find_common_elements(list1, list2, case_sensitive=True):
    if not case_sensitive:
        list1 = [x.lower() if isinstance(x, str) else x for x in list1]
        list2 = [x.lower() if isinstance(x, str) else x for x in list2]
    x = []
    for i in list1:
        if i in list2:
            x.append(i)
    return x

find_common_elements([1, 2, 3, 'Apple'], [3, 4, 'apple'], case_sensitive=False)

# 41. Enhanced exception handling demo
def handle_file_operations(filename):
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        print(f"File content: \n\n{content[:50]}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
    finally:
        if file is not None:
            file.close()
            print("File handle closed")

handle_file_operations('50Ques/Q41.txt')

# 42. JSON parser with validation

import json
def parse_json(json_string):
    try:
        data = json.loads(json_string)
        print("Valid structure is Valid:")
        return data
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {str(e)}")
        return None

parse_json('{"name": "John", "age": 30, "city": "New York"}')

# 43. Class with private/protected members
class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self._account_number = self._generate_account_number()
        self.__balance = initial_balance
    
    def _generate_account_number(self):
        import random
        return f"ACCT-{random.randint(100000, 999999)}"
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

account = BankAccount("John Doe", 1000)
account.account_holder, account._account_number, account.get_balance()

# 44. Email validator with comprehensive checks
def is_valid_email(email):
    import re
    pattern = r"""
        ^                      
        [a-zA-Z0-9._%+-]+       
        @                       
        [a-zA-Z0-9.-]+          
        \.                      
        [a-zA-Z]{2,}            
        $                       
    """
    if not re.match(pattern, email, re.VERBOSE):
        return False
    
    if '..' in email or email.startswith('.') or email.endswith('.'):
        return False
    
    return True

is_valid_email("john.doe@example.com"), is_valid_email("invalid@.com")

# 45. CSV to dictionaries converter with error handling
def csv_to_dicts(csv_file, delimiter=','):
    import csv
    try:
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=delimiter)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found")
        return []
    except Exception as e:
        print(f"Error processing CSV: {str(e)}")
        return []

csv_to_dicts('../Docs/Electric Vehicle Sales by State in India.csv')

# 46. Enhanced login system with multiple attempts
def login_system():
    import getpass
    
    users = {
        "admin": {"password": "secure123", "role": "administrator"},
        "user1": {"password": "mypass", "role": "regular"}
    }
    
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        
        if username in users and users[username]["password"] == password:
            print(f"Welcome {username}! Role: {users[username]['role']}")
            return True
        
        attempts += 1
        remaining = max_attempts - attempts
        print(f"Invalid credentials. {remaining} attempts remaining.")
    
    print("Maximum attempts reached. Access denied.")
    return False

login_system()

# 47. Enhanced list flattener with type checking
def flatten_list(nested, output=None):
    if output is None:
        output = []
    
    for item in nested:
        if isinstance(item, (list, tuple)):
            flatten_list(item, output)
        else:
            output.append(item)
    return output

flatten_list([1, [2, [3, 4], 5], 6, (7, 8)])

# 48. Functional programming operations demo
def demonstrate_functional_operations():
    from functools import reduce
    
    numbers = list(range(1, 11))
    
    number_words = ['zero', 'one', 'two', 'three', 'four', 
                   'five', 'six', 'seven', 'eight', 'nine', 'ten']
    mapped = list(map(lambda x: number_words[x], numbers))
    
    filtered = list(filter(lambda x: x % 3 == 0, numbers))
    
    reduced = reduce(lambda x, y: x * y, numbers[:5])
    
    return {
        'original': numbers,
        'mapped': mapped,
        'filtered': filtered,
        'factorial_5': reduced
    }

demonstrate_functional_operations()

# 49. Enhanced CLI calculator
def interactive_calculator():
    history = []
    
    print("Interactive Calculator (type 'quit' to exit)")
    
    while True:
        try:
            expression = input("> ").strip()
            
            if expression.lower() in ('quit', 'exit'):
                break
            if not expression:
                continue
            if expression.lower() == 'history':
                print("\nCalculation History:")
                for i, item in enumerate(history, 1):
                    print(f"{i}. {item['expr']} = {item['result']}")
                continue
            
            # Safety check - only allow certain characters
            if not all(c in '0123456789+-*/. ()' for c in expression):
                print("Error: Only numbers and +-*/. operators allowed")
                continue
            
            result = eval(expression)  # Caution: eval can be dangerous in real apps
            history.append({'expr': expression, 'result': result})
            print(result)
            
        except Exception as e:
            print(f"Error: {str(e)}")
    
    print("\nFinal History:")
    for i, item in enumerate(history, 1):
        print(f"{i}. {item['expr']} = {item['result']}")

interactive_calculator()

# 50. Comprehensive quiz system
def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Paris", "Berlin", "Madrid"],
            "answer": 1,
            "explanation": "Paris has been the capital of France since the 12th century."
        },
        {
            "question": "Which of these is NOT a Python data type?",
            "options": ["int", "str", "decimal", "float"],
            "answer": 2,
            "explanation": "Python has 'int', 'str', and 'float' but not 'decimal' as a basic type."
        }
    ]
    
    score = 0
    print("Welcome to the Python Quiz!\n")
    
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for idx, option in enumerate(q['options'], 1):
            print(f"  {idx}. {option}")
        
        while True:
            try:
                answer = int(input("Your answer (number): ")) - 1
                if 0 <= answer < len(q['options']):
                    break
                print(f"Please enter a number between 1-{len(q['options'])}")
            except ValueError:
                print("Please enter a valid number")
        
        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. {q['explanation']}")
        
        print()  # Blank line
    
    print(f"\nQuiz complete! Your score: {score}/{len(questions)}")
    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    if percentage >= 80:
        print("Excellent performance!")
    elif percentage >= 60:
        print("Good job!")
    else:
        print("Keep practicing!")

run_quiz()