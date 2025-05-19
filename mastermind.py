#hiiiiiiiiii
import random


def gamenumber():
    numlist = []
    difficulty = input("How long: ")

    while True:
        if difficulty.isnumeric():
            #print("IS number")
            break
        
    for i in range(int(difficulty)):
            numlist.append(random.randint(0,9))
    return numlist



while True:
    print(gamenumber())
    
