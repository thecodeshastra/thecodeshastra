import random


def main():
    UserLevel = get_level()
    Scored = generate_integer(UserLevel)
    print(f"Score: {Scored}")

def get_level():
    while True:
        try:
            UL = int(input("Level: "))
            if UL in range(1,4):
                return UL
            else:
                continue
        except ValueError:
            continue

def generate_integer(level):
    score = 0
    if level == 1:
        for i in range(1,11):
            x = random.randint(0,9)
            y = random.randint(0,9)
            z = x + y
            for i in range(1,4):
                try:
                    U = int(input(f"{x} + {y} = "))
                    if U == z:
                        score = score + 1
                        break
                    else:
                        print("EEE")
                except ValueError:
                    print("EEE")
                if i == 3 and U != z:
                    print(f"{x} + {y} = {z}")
        return score
    elif level == 2:
        for i in range(1,11):
            x = random.randint(10,99)
            y = random.randint(10,99)
            z = x + y
            for i in range(1,4):
                try:
                    U = int(input(f"{x} + {y} = "))
                    if U == z:
                        score = score + 1
                        break
                    else:
                        print("EEE")
                except ValueError:
                    print("EEE")
                if i == 3 and U != z:
                    print(f"{x} + {y} = {z}")
        return score
    else:
        for i in range(1,11):
            x = random.randint(100,999)
            y = random.randint(100,999)
            z = x + y
            for i in range(1,4):
                try:
                    U = int(input(f"{x} + {y} = "))
                    if U == z:
                        score = score + 1
                        break
                    else:
                        print("EEE")
                except ValueError:
                    print("EEE")
                if i == 3 and U != z:
                    print(f"{x} + {y} = {z}")
        return score



if __name__ == "__main__":
    main()