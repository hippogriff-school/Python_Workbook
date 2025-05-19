import random

ans = random.randint(0,99)

guess = int(input("What is your guess? (0-99): "))

if guess[0:] == ans[0:]:
    print("")
