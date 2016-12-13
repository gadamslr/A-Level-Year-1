# GTIN Programming challenge Task 2

# Import the CSV module.
import csv

# initiating my variables
csvFile = 'GTINprodDetails.csv'

def writeToCSV(csvFile):
    # Must open a csv file and assign it to a file-object
    try:
        myFile = open(csvFile, 'a')
    except IOError:
        print("Create file")
        myFile = open(csvFile, 'w')
        
        

    #This sets up headers in the CSV file
    myDictHeaders = ['GTIN8','Description', 'Price']

    # Creates a writer-object which maps the parameters onto the output rowa
        # csvFile = the name of your file-object
        # fieldnames = the list you created for the CSV file headers
        # lineterminator defaults to \r\n  with this added you can stop the escape sequences /r/n being added
        # I have chosen to remove the \n (new line) escape sequence and just have the carriage return. This means the nextline will appear on the next line.
    writeObject = csv.DictWriter(myFile, fieldnames=myDictHeaders, lineterminator = '\n')

    writeObject.writeheader()

    # To write to the csv file we use writerow, a method from the used from the write-object.
    addProduct = True
    
    while addProduct == True: 
        gtinCode = gtinCheck()
        prodDesc = input("Enter product description: ")
        prodPrice = input("Enter product price: ")

        writeObject.writerow({"GTIN8": gtinCode, "Description": prodDesc, "Price": prodPrice}) # As only one argument can be written, the two arguments are put in a parenthesis, and is seperated by a comma. can 

        x = input("Do you want to continue? (y/n)")
        if x != "y":
            addProduct = False
        
    # Closing the file-object - this will save the data written to the csv file.
    myFile.close()

def gtinCheck():
    # Initialise variables
    GTINcheck = False
    gtinList = []
    checkDigit = 0

    # Checks that the GTIN number entered is valid
    while GTINcheck == False:
        gtinNum = input("Enter product GTIN8 code: ")
        try: # Validation check to ensure the value entered is numeric.
                    if int(gtinNum) and (6 < len(gtinNum) < 9 ):
                            gtinList = list(gtinNum)
                            GTINcheck = True
        except ValueError: #If value entered is non-numeric then inform user
                    print("GTIN should be numeric")
                    print("Try again")
                    
    #print("GTIN number entered is: ",gtinList)

    # Counter to perform the main algorithm for task 1
    counter = 0
    calc = 0
    for counter in range(0,7): # Loops from 0 upto, not including the 7th GTIN digit
            x = int(gtinList[counter]) 
            if (counter % 2) == 1:
                calc +=(x * 1)
            else:
                calc +=(x * 3)

    # To calculate the nearest multiple of 10 I have used a counter
    while (calc + checkDigit) %10!=0:
            checkDigit += 1

    # Test to see if the eigth digit is present.
    if len(gtinNum) == 8: # If GTIN num entered = 8 digits
            if int(checkDigit) == int(gtinNum[7]):
                    print("GTIN8 checkDigit is valid: {} ".format (checkDigit))
            else:
                    print("GTIN8 checkDigit is not valid: {}".format (gtinNum[7]))
    else:
        print("Therefore check digit is: {}".format (checkDigit))
        gtinNum = gtinNum + checkDigit

    return(gtinNum)

def readCSVToDict(csvFile):
    # Initialising my dictionary
    myDict = {}
    
    myFile = open(csvFile, 'r')
    
    # Need to create a read-object.
    readObject = csv.DictReader(myFile)

    # Reading the headers of my csv file as I have come.
    headers = readObject.fieldnames

    # Printing my headers - "index","FirstName", "SurName"
#    print(headers)

    # Mapping the headers as keys and appending data to my Dictionary
    for row in readObject:
        myDict[row["GTIN8"]] = [row["Description"], row["Price"]]

    # Closing the file-object - this will closes the opened csv file.
    myFile.close()

    return(myDict)

def printCSVDict(myDict):
    # Printing my dictionary
    for key, value in myDict.items():
        print(key, value)


def searchProducts(myDict):
    searchGTIN = input("Enter GTIN to search for")
    # Printing the dictionary values when key value i
    print("Product info on {}, {}".format (searchGTIN, myDict[searchGTIN]))


def prodPurchases(myDict):
    anotherPurchase = True
    purchaseList = []
    while anotherPurchase == True:
        prodPurchase = input("Enter GTIN8 code of product you want to purchase")
        prodQuantity = input(("Enter the quantity of {} you want to purchase").format(prodPurchase))
        if prodPurchase in myDict:
            purchaseList.append([prodPurchase, (myDict[prodPurchase][0]), (myDict[prodPurchase][1]),prodQuantity])
        else:
            purchaseList.append(prodPurchase, "product not found")
        nextItem = input("Do you want to purchase another item?")
        if (nextItem[0]).lower() != "y":
            anotherPurchase = False
    purchaseReceipt(purchaseList)


def purchaseReceipt(purchList):
    totalCostofOrder = 0
    subTotal = 0
    for entity in purchList:
        subTotal = round(float(entity[2])* float(entity[3]),2)
#        print(subTotal)
#        print(entity)
        print(("{0}    {1}             {2}    {3}    {4}").format(entity[0], entity[1], entity[2], entity[3], str(subTotal)))
        totalCostofOrder +=  subTotal
    print("Total cost of order                     {}".format(totalCostofOrder))

def menu():
    exitMenu = False
    prodDict = readCSVToDict(csvFile)
    while exitMenu == False:
        menuSelection = int(input("Choose from\n\
    1 - Add new product details\n\
    2 - List products\n\
    3 - Search for a product\n\
    4 - Purchase products\n\
    5 - Quit\n\
    \n\
    Enter option number: "))
        if menuSelection == 1:
            writeToCSV(csvFile)
            prodDict = readCSVToDict(csvFile)
        elif menuSelection == 2:
            printCSVDict(prodDict)
        elif menuSelection == 3:
            searchProducts(prodDict)                
        elif menuSelection == 4:
            prodPurchases(prodDict)
        elif menuSelection == 5:
            x = input("Press Q to quit.")
            if x.lower() == "q":
                exitMenu = True


if __name__ == "__main__":
    # execute only if run as a script
    menu()
