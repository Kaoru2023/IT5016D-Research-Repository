# FibonacciUsingWhile.py
#
# author: Kaoru
# date 13.08.23


print("\nThe Fibonacci Sequence:\n")
p = "0"
while int(p) < 3:
    p = input("Please enter a number corresponding to the position in the sequence(should be at least 3:)")

q = 0
while q <= 0:
    q = int(input("Please enter number of terms to generate (should be a positive integer): "))

print("\n", q, "numbers in the sequence starting from term ", p, ":")

# convert p and q to integers
p, q = int(p), int(q)

# initialise term counters to zero
p_counter, q_counter = 2, 0

# initialise the first two terms in the sequence
n1, n2 = 0, 1

while q_counter < q:
    nth = n1 + n2
    n1, n2 = n2, nth
    p_counter += 1
    if p_counter >= p:
        q_counter += 1
        if q_counter < q:
            print(nth, end = ", ")
        else:
          print(nth)

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_recursive(n):
    print("Calculating F", "(", n, ")", sep="", end=", ")

    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

fibonacci_recursive(5)