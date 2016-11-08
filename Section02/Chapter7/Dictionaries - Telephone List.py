# Dictionaries - Telephone List

myPhoneDict = { 'Mum': '0123456789',
                'Sis': '0123456452',
                'Pete': '0123456452',
                'Mary': "0787654321" }

for contactName, phoneNum in myPhoneDict.items():
    # Print all the values
    print( "My key for dictionary is ", contactName, " and the value is ", phoneNum )



#To sort the key values in a dictionary 
"""
myContacts = sorted(list(myPhoneDict.keys()))
print (myContacts)
"""
