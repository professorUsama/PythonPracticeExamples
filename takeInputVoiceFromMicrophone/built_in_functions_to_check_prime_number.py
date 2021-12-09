#Method 1

# import sympy

# user_input_number = int(input("Enter number to check prime or not: "))
# print(sympy.isprime(user_input_number)) # the output in the boolean True of False
# if sympy.isprime(user_input_number) is True:
#     print(f"{user_input_number} is prime")
# else:
#     print(f"{user_input_number} is not prime")

# from sympy import isprime
# user_input_number = int(input("Enter number to check prime or not: "))
# if isprime(user_input_number) is True:
#     print(f"{user_input_number} is prime")
# else:
#     print(f"{user_input_number} is not prime")

#method 2 ======================

from primePy import primes
user_input_number = int(input("Enter number to check prime or not: "))
if primes.check(user_input_number) is True:
    print(f"{user_input_number} is prime")
else:
    print(f"{user_input_number} is not prime")
