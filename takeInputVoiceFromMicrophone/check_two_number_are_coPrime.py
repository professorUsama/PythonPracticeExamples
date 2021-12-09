# from math import gcd

# def isCoPrime(a,b):
#     return gcd(a,b) == 1


# if __name__ == '__main__':
#     a , b = map(int,input("Enter the value of a and b: ").split())
#     if isCoPrime(a,b) is True:
#         print(f"{a} and {b} is co-prime")
#     else:
#         print(f"{a} and {b} is co-prime")

# res = gcd()
# print(res)

from sympy import factor
from sympy import factorint
from sympy import factor_list
# ans = factor()
# ans = factorint(44)
ans = factor_list(44)
print(ans)