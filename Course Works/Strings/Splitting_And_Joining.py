# Splitting_And_Joining.py
#
# author: Kaoru
# date: 01.09.23

# more practice on splitting and joining
s = "This is a long string with a bunch of words in it."
# split with default deliminator
print(s.split())
# defining variables, to first split the string, and then joining the splitted string with space, :, and --
l = s.split()
s2 = ':'.join(l)
s3 = ' -- '.join(l)
print(' '.join(l))
print(s2)
print(s3)