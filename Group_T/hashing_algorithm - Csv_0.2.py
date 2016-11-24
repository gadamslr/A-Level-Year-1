import csv

stuDict = {}
keepGoing = True
#maxStudents = int(input("Enter the maximum number of students allowed in a class:"))
maxStudents = 20
print("Maximum number of students in a class set to {0}:".format(maxStudents))


def hashUserID(stuName):
    global maxStudents
    count = 0

    for element in list(stuName):
        count += ord(element)

    print(count)

    index = count % maxStudents

    print("index = ", index)

    return(index)


def hashPassword(stuPassword):
    global maxStudents
    counter = 0
    
    for element in list(stuPassword):
            counter += ord(element)

    print(counter)
    hashedPwd = str(hex(counter % maxStudents))

    print("Hashed password = ", hashedPwd)

    return(hashedPwd)

    

def addStudents():
    xDict = {}
    hashStuPwd = 0
    stuName = input("Enter the name of a student:")
    stuPassword = input("Enter a password:")
    stuDOB = input("Enter your D.O.B:")

    index = hashUserID(stuName)
    hashStuPwd = hashPassword(stuPassword)

    xDict[index] = [stuName, hashStuPwd, stuDOB]

    print(xDict)

    addToCSV(index, stuName, stuPassword)

    return(xDict)


def outputStudents(stuDict):
    print(stuDict)


def addToCSV(index, stuName, stuPassword):

    global maxStudents
    
    with open("hashTable.csv", "w+", newline='') as csvFile:
        newData = csv.writer(csvFile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        #Check for index number in csv file
        for row in csvFile:
            if index == row[0]:
                print(row[1])
                print("Collision!!")

        #Resetting the pointer following the index number search
        csvFile.seek(0)
        
        for x in range(maxStudents):
            if x == index:
                newData.writerow((index, stuName, stuPassword))
            else:
                newData.writerow(((x),))
                

def checkPassword():
    stuName = input("Enter student name:")
    stuPassword = input("Enter password:")
    count = 0
    
    for element in list(stuPassword):
        count += ord(element)

    index = count % maxStudents
    
    with open("hashTable.csv", "rb") as csvFile:
        for row in range(maxStudents):
            if row == index:
                newData = csv.reader(csvFile, delimiter=',', quotechar=',')
                print(list(newData))



def menu():
    choice = int(input("Choose from the following options:\n\
1 - Add a new student\n\
2 - View students in array\n\
3 - Check password\n\
4 - Exit\n\
:"))
    if choice == 1:
        stuDict.update(addStudents())
    elif choice == 2:
        outputStudents(stuDict)
    elif choice == 3:
        checkPassword()
    elif choice == 4:
                    
        return(False)

    return(True)

while keepGoing == True:
    keepGoing = menu()
