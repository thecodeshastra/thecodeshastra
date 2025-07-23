import random

def main():
    Level = userLevel()
    RG = random.randint(1,Level)
    check(RG)


def userLevel():
    while True:
        try:
            UL = int(input("Level: "))
            if UL < 1:
                continue
        except ValueError:
            continue
        else:
            return UL


def check(a):
    while True:
        try:
            UG = int(input("Guess: "))
            if UG == a:
                print("Just right!")
                break
            elif UG > a:
                print("Too large!")
                continue
            elif UG < a:
                print("Too small!")
                continue
        except ValueError:
            continue


main()