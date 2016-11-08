print ('Welcome to Pypet!')

# Set up a dictionary with all details relating to our pet cat
cat = {
  'name': 'Fluffy',
  'hungry': True,
  'weight': 9.5,
  'age': 5,
  'photo': '(=^o.o^=)_',
}

# Set up a dictionary with all details relating to our pet mouse
mouse = {
    'name': 'Mouse',
    'age': 6,
    'weight': 1.5,
    'hungry': False,
    'photo': '<:3 )~~~~',
}

# A list of dictionary elements - a list of all our pets
pets = [cat, mouse]

#
# Function feed
# This function will check whether this pet is hungry
# If it is hungry, then it will 'feed' the pet
# which will increase the pets weight
#
# Parameter - pet, which is a dictionary
#
def feed(pet):
    if pet['hungry'] == True:
        # Our pet is hungry - increase the weight
        pet['hungry'] = False
        pet['weight'] = pet['weight'] + 1
        print ('omnomom!!')

    else:
        print ('The Pypet is not hungry!')

#
# Main code here
#
for pet in pets:
    # Print out the pet details and then try and feed the pet
    print ('------------------------------')
    print ('Hello ' + pet['name'] + '!')
    print (pet['photo'])
    print ('Weight: ' + str(pet['weight']))
    # Call the function to feed the pet
    feed(pet)
    # The pets weight will have increased if it was fed
    print ('Weight: ' + str(pet['weight']))
    print ('------------------------------')

