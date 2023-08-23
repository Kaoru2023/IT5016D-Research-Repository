# ForLoopNumberFinder.py
#
# author: Kaoru
# date: 14.08.23

# Learning activity 39 - finding numbers divisible by 7 and multiples of 5,
#between 1500 and 2700(both included)

nl=[]
for i in range(1500, 2700+1,):
    if(i%7==0) and (i%5==0):
#        nl.append(i)
#        nl.append(str(i))
#    print(",".join(nl))
     print(i, end=", ")
