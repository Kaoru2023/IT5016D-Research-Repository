# Functions_learning_Scope.py
#
# author: Kaoru
# date: 24.08.23

# testing how python react when calling the local variable outside of the function
# 'asserting it throws an error that says name is not defined
'''def test_name():
    name = Kaoru
    return name

print(name)'''


# now, creating a Global variable
# 'asserting now it returns 'Suzuki' and 'Kaoru'
name = 'Suzuki'
def test_name():
    name = 'Kaoru'
    return name

print(name)
print(test_name())