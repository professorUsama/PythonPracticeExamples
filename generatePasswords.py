import random

if __name__ == '__main__':
    length_code = int(input("Enter the length of Password: "))
    mix_string = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    list_password = random.sample(mix_string,length_code)
    print(list_password)
    password = "".join(list_password)
    print(password)