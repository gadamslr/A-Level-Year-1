#james
+print("a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort")
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
# Divides left hand operand by right hand operand and returns remainder
    index = count % slots

    print("index = ", index)

    tempDict[index] = stuName

    print(tempDict)

    return(tempDict)

#function to print out the dictionary
def outputStuents(stuDict):
    print(stuDict) #outputs the dictionary "stuDict"

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




