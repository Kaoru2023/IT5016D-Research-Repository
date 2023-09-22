# GrammarScEntryCriteria.py
#
# autor: Kaoru
# 05.08.23

# Activity Challenge 1
'''
I run a small grammar school in Auckland. I need a program that lets me know whether a student can enroll in our school. There are some conditions that must be met for each application.

The program must check that the student:

·         Lives less than 4 km from the school

·         Is under 18 years old

·         Has the right to stay in New Zealand

However, if a student is under 18, and will pay international student fees, then they can enroll.
'''
# FROM TEXT BOOK
distance_from_school = 3
age_in_years = 14
has_residency = True
is_fee_foreign = False
print("This program works out eligibility for enrolment...\n")

# Test assertion 3: result should be True
print("The student's eligibility to enrol is ",
      distance_from_school < 4
      and age_in_years < 18
      and has_residency
      or age_in_years < 18
      and is_fee_foreign, "\n")

print("The student waited for too long...\n")
age_in_years = 18

# Test ssertion 4: result should be False
print("The student's eligibility to enrol now is ",
      distance_from_school < 4
      and age_in_years < 18
      and has_residency
      or age_in_years < 18
      and is_fee_foreign, "\n")


# now trying interactive version, including prompts for user input.
# The input should be used to set the distance and age variables,
# residency status, and fee payment  
# The requirements have been amended, the students should be less than
# 18 years old but older than 10. 
distance_from_school = int(input("Please enter distance from school\n"))
age_in_years = int(input("Please enter your age ,\n"))
has_residency = bool(input("Has residency? Please enter Y or N ,\n") == "Y")
is_fee_foreign = bool(input("Paying international fee? Please enter Y or N ,\n") == "Y")
print("This program works out eligibility for enrolment...\n")

print("Your eligibility to enrol is ",
      distance_from_school < 4
      and age_in_years < 18
      and age_in_years > 10
      and has_residency
      or is_fee_foreign,"\n")

