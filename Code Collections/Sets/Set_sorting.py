# Set_sorting.py
#
# author: Kaoru
# date: 22.08.23

# set of all friends
friends = set(['Dillon', 'Kyle', 'Rae', 'Bill', 'Larry', 'Connie', 'Aaron',
              'Jim', 'Brandon', 'Frank', 'Verne', 'Garry', 'Landon', 'Tom',
              'Olivia', 'Richard', 'Bruice', 'David', 'Katy', 'Mark'])

# set of people who live in my zip code
zipcode = set(['Jerry', 'Elaine', 'Cindy', 'Verne', 'Rudolph', 'Bill', 'Olivia',
               'Jim', 'Lindsay', 'rae', 'Mark', 'Kramer', 'Landon', 'Newman',
               'George'])

# set of people who play Chess
chess = set(['Steve', 'Jackson', 'Frank', 'Bill', 'Mark', 'Landon', 'Rae'])

# set of Olivia's friends
olivia = set(['Jim', 'Amanda', 'Nestor'])

# sorting these friends
# finding my local friends, use 'intersection' operator on the set of all friends
# and pass it the set of people on zipcode as an argument
# asser output a set of friends who belongs to all friends and zipcode people
# try it interchangably
local = friends.intersection(zipcode)
print(local)
local = zipcode.intersection(friends)
print(local)


# remove friends who play chess from local friends by calling "difference" operator
# on the set of local friends, and pass it to a set of chess players as an argument
# assert output a set of friends in local who is not chess players
invite = local.difference(chess)
print(invite)

# calling "difference" operator on a chess set and pass it to local
# assert output totaly different set of people now, chess players but not local
#invite = chess.difference(local)
#print(invite)

# revising the invite set by removing any friends in common with Olivia's friend
# leaving just the unique names behind, using symmetric_difference operator
invite = invite.symmetric_difference(olivia)
print(invite)

# checking if Jerry is in invite set
# assert  output False as Jerry is not in invite set
print('Jerry' in invite)

# Adding Jerry to invite set bu calling "add" operator passing Jerry as the argument
invite.add('Jerry')
print(invite)

# removing Amanda by calling "remove" method on th einvite list
invite.remove("Amanda")
print(invite)

# using pop method to pulling out people in invite set
# assert  output error when set reaches empty 
print(invite.pop())
print(invite.pop())
print(invite.pop())
print(invite.pop())
print(invite.pop())



