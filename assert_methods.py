import math

# This is a Boolean-valued function, also known as a predicate function, 
# that returns True if the input number is prime and False otherwise.

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True