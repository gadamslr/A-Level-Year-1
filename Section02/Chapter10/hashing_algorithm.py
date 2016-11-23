stuDict = {}
keepGoing = True
maxStudents = int(input("Enter the maximum number of students allowed in a class:"))

def addStudents():
    global maxStudents
    count = 0
    xDict = {}
    stuName = input("Enter the name of a student:")

    for element in list(stuName):
        count += ord(element)

    print(count)

    index = count % maxStudents

    print("index = ", index)

    xDict[index] = stuName

    print(xDict)

    return(xDict)


def outputStuents(stuDict):
    print(stuDict)

def menu():
    choice = int(input("Choose from the following options:\n\
1 - Add a new student\n\
2 - View students in array\n\
3 - Exit\n\
:"))
    if choice == 1:
        stuDict.update(addStudents())
    elif choice == 2:
        outputStuents(stuDict)
    elif choice == 3:
        return(False)

    return(True)

while keepGoing == True:
    keepGoing = menu()
