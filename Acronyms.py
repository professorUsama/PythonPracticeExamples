# acronyms means mukhafaf

if __name__ == '__main__':
    user_input = input("Enter Pharse: ").split() # user_input with split function return a list
    word = "" # to store the 1st latter of each words
    for latter in user_input:
        word += latter[0].upper()
    print(word)