# get_score_Functions.py
#
# author: Kaoru
# date: 20.09.23

# Write a short 2 question quiz that uses a function to evaluate each answer
# and return a score.

score = 0


def get_score(question, answer, score):
    print(question)
    user_input = input("Answer: ")
    if user_input == answer:
        score += 1
        print("Well Done!")
    else:
        print("Wrong answer...")
    return score


score = get_score("Name of the capital city of New Zealand?",
                  "Wellington", 0)
score = get_score("Name of the capital city of Japan?",
                  "Tokyo", score)
print(f"Your score: {score}")

'''
assertion
input Wellington and Tokyo
print "Well Done" and return score 2

input Wellington and Osaka
first print "Well Done!" and second "Wrong answer..." then return 1

'''
