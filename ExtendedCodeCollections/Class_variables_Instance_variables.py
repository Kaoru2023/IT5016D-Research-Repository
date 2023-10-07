# Class_variables_Instance_variables.py
#
# author: Kaoru
# date: 28.09.23

class Employee:
    # create class variables
    num_of_emps = 0
    raise_rate = 1.05

    def __init__(self, first_name, last_name, wage):
        self.first_name = first_name
        self.last_name = last_name
        self.wage = wage
        self.email = first_name.lower() + '.' + last_name.lower() + '@gmail.com'

        # each time creating an employee=instance, increment 1
        # do it in init method, since init method run every time creating an instance
        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self) -> object:
        self.wage = int(self.wage * self.raise_rate)

    # define classmethod
    # this is the same thing as changing/defining class variable
    # "raise rate = 1.06
    @classmethod
    def set_raise_rate(cls, rate):
        cls.raise_rate = rate

    # create a classmethod as alternative constructor
    # when using a list of string of info of new employees
    @classmethod
    def from_string(cls, emp_str):
        first_name, last_name, wage = emp_str.split('-')
        return cls(first_name, last_name, wage)

    @staticmethod
    # static method don't take instance or class arguments
    # can take any arguments like functions
    def is_workday(day):
        # Python starts days  from 0, Mon=0, Tue=1
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True


print(Employee.num_of_emps)

emp_1 = Employee('Taro', 'Tanaka', 30000)
emp_2 = Employee('Hanako', 'Sato', 40000)

print(emp_2.fullname(),
      emp_2.email,
      sep="\n"
      )

emp_1.apply_raise()

print(emp_1.raise_rate,
      emp_1.wage,
      sep='\n',
      )

print(Employee.raise_rate,
      emp_1.wage,
      sep='\n',
      )

print(emp_2.raise_rate,
      emp_2.wage,
      sep='\n',
      )

print(Employee.num_of_emps)

# run classmethod to set the new raise rate
Employee.set_raise_rate(1.06)

print(emp_1.raise_rate,
      emp_2.raise_rate,
      sep="\n"
      )
# instead of running classmethod, changing raise rate
Employee.raise_rate = 1.07

print(emp_1.raise_rate,
      emp_2.raise_rate,
      sep="\n"
      )

# using classmethod as constructor
emp_str_1 = "Jiro-Takeda-15000"
emp_str_2 = "Nanako-Oda-20000"

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email,
      new_emp_1.wage,
      sep='\n',
      )

print(Employee.num_of_emps)

new_emp_2 = Employee.from_string(emp_str_2)

print(new_emp_2.email,
      new_emp_2.wage,
      sep='\n',
      )

print(Employee.num_of_emps)


from datetime import date

my_date = date.today()

print(my_date)

print(Employee.is_workday(my_date))

'''
assertion
output
no instance yet
0
created instance
Hanako Sato
Hanako.Sato@gmail.com
applied pay raise to instance variable
1.05
31500
using class variable
1.05
31500

1.05
40000
number of instances created so far
2
classmethod
1.06
1.06
reset class variable
1.07
1.07
construct with classmethod
Jiro.Takeda@gmail.com
15000
numbers of instances so far
3
Nanako.Oda@gmail.com
20000
4
run staticmethod
2023-09-28
True
'''
