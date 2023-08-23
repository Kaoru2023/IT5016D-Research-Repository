# Dictionary_Learning.py
#
# authod: Kaoru
# date:22.08.23

dictionary_1 = {"shirt":50,
                "skirt":80,
                "bag":150}

# retrieving a value from dictionary
print("The shirt is worth $" + str(dictionary_1["shirt"]))

# create a mapping of state to abbreviation
states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
}

# add some more cities
cities['NY'] = 'New york'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

# print out some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has; ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
# This for statement creates and sets 2 new variables called state and abbrev
#(These are separated by a comma). The "states" dictionary item key and
# item value are used to set the variables.
# Also, the <string>.format( <value> , <value>) syntax is used
# to insert the values of state and abbrev into a string.
# This is the preferred approach for putting variables into strings.
# Notice too that this is zero based, the first string to be used is defined
#by {0}.
print('-' * 10)
for state, abbrev in states.items():
    print("{0} is abbreviated {1}".format(state, abbrev))

# now do both at the same time
print('-' * 10)
for state, abbrev in states.items():
    print("{0} state is abbreviated {1} and has city {2}".format(
        state, abbrev, cities[abbrev]))

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is: {0}".format(city))

          # get a city with a 
