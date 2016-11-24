stuDict = {}
keepGoing = True
slots = int(input("The numbers of SLOTS in your array /  data table:"))

def addStudents():
    global slots
    count = 0
    tempDict = {}
    stuName = input("Enter the name of a student:")

    # Convert each letter in the inputted name into the ascii code and add them together
    for element in list(stuName):
        count += ord(element)

    print(count)

    index = count % slots

    print("index = ", index)

    tempDict[index] = stuName

    print(tempDict)

    return(tempDict)


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




