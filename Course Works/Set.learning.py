# Set.learning.py
#
# author: Kaoru
# date: 18.08.23

# The order doesn't matter for "Set", but set has unique items.

''' creating and combining Sets of friends Using Set Function '''

college = set(['Bill', 'Katy', 'Verne', 'Dillon',
               'Bruice', 'Olivia', 'Richard', 'Jim'])
coworker = set(['Aaron', 'Bill', 'Brandon', 'David',
                'Frank', 'Connie', 'Kyle', 'Olivia'])
family = set(['Garry', 'Landon', 'Larry', 'Mark',
              'Olivia', 'Katy', 'Rae', 'Tom'])

# I can check items in each set, or numbers of items in each set
print(college)
print(len(coworker))

# Combining sets by calling union method to create a single set
friends = college.union(coworker,family)
print(friends)
# The union operator removed the duplicate names, making a set which has unique items
print(len(friends))


