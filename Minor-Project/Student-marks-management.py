students = {"name":["Vaman","lakshay"],'marks':[98.5,100]}


def addStudent():
    name = input("\n\n\nEnter the name of student")
    marks = float(input("Enter marks"))
    if name in students["name"]:
        print("Student Already Present in Data")
    else:
        students["name"].insert(len(students["name"]),name)
        students["marks"].insert(len(students["marks"]),marks)
    print(students['name'],students['marks'])
def updateMarks():
    name = input("\n\n\nEnter the name of student")
    if name in students["name"]:
        marks = float(input("Enter marks"))
        students['marks'][students["name"].index(name)] = marks
        print(name,students['marks'][students["name"].index(name)])
    else:
        print("Student not found")
    

def showMarks():
    name = input("\n\n\nEnter the name of student")
    if name in students["name"]:
        print(students['marks'][students["name"].index(name)])
    else:
        print("Student Not Found")

def allMarks():
    maxMarks = 0
    for marks in students['marks']:
        if marks > maxMarks:
            maxMarks = marks
    print("Maximum Marks = ",maxMarks)
    minMarks = maxMarks
    for marks in students['marks']:
        if marks < maxMarks:
            maxMarks = marks
    print("Minimum Marks = ",maxMarks)
    averageMarks = 0
    for marks in students['marks']:
        averageMarks += marks
    averageMarks = averageMarks / len(students['marks'])
    print("Average Marks = ",averageMarks)
    

def display():
    print("\n\n\nName:\t Marks")
    for i in students['name']:
        print(i,':\t',students['marks'][students['name'].index(i)])

# save = open("studentdata.txt",'w')
# save.write(students)
while True:
    option = int(input("\n\n\nEnter the task to perform\n\t1. Add Student\n\t2. Update Student\n\t3. Show Marks\n\t4. Display highest, lowest, and average marks\n\t5. Show All Students\n\t0. Exit\n\t"))
    match option:
        case 1:
            addStudent()
            
        case 2:
            updateMarks()
            
        case 3:
            showMarks()
            
        case 4:
            allMarks()

        case 5:
            display()
            
        case _:
            break
            