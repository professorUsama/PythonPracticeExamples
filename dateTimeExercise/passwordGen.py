from random import choice
import random
import math
# upper = "abcdefghijklmnopqrstuvwxyz"
# lower = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
# pass_ = ""
# print(choice(lower))
# for password in range(1,7):
#     pass_ = pass_ + choice(lower)

# print(pass_)
digits = "0123456789"
OTP = ""
OTP += digits[math.floor(random.random() * 10)] 

print(OTP)
