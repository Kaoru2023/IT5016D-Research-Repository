# Lists_activities40_DaysOfTheWeek.py
#
# author: Kaoru
# date: 17.08.23

Days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]


#print(len(Days))
#print(Days)

#Print the 2nd and 5th days of the week in the console
#assertion output "Tue Fri"
print(Days[1],Days[4])

# try loop
# assertion output "Tue, Fri"
Display = [1, 4]
count = 1
while len(Display) >= count:
    if len(Display) == count:
       print(Days[Display[count-1]])
    else:
        print(Days[Display[count-1]], end=', ')
    count += 1

# Print the day of the week that is 3 days from the end of the week
# assertion output "Fri"
print(Days[-3])

# trying more
# assertion output "Tue, Wed, Thu, Sat, Sun" 
Display = [1, 2, 3, 5, 6]
count = 1
while len(Display) >= count:
    if len(Display) == count:
       print(Days[Display[count-1]])
    else:
        print(Days[Display[count-1]], end=', ')
    count += 1
