# ShoeSize,py
#
# autor: Administrator
# date: 05.08.23

my_size = 7.5
print("The pype of my_size is ", type(my_size),"\n")
print("My shoe size is ", my_size,"\n")

print("Casting to an integer...\n")
# variable cast to integer
my_size = int(my_size)

print("The type of my_size is now ", type(my_size),"\n")
print("My shoe size is ", my_size, "\n")

x = False
y = True

print(type(x))

x = ["J","b","s"]
print(type(x))

x = ("b","L", "m")
print(type(x))

x = {"a":"1","b":"2","c":"3"}
print(type(x))

x=5
y=x
print("x=",x,"y=",y)
x=10
print("x=",x,"y=",y)
