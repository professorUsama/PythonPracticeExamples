from random import randint

if __name__ == '__main__':
    while(True):
        input("press enter to roll the dice...\n")
        dice = randint(1,6)
        print(dice)
        if dice == 6:
            break