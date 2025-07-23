import random


def main():
    UserLevel = get_level()
    score = 0
    for i in range(1,11):
        x,y,z = generate_integer(UserLevel)
        for i in range(1,4):
            try:
                U = int(input(f"{x} + {y} = "))
                if U == z:
                    score = score + 1
                    break
                else:
                    print("EEE")
            except:
                print("EEE")
            if i == 3 and U != z:
                print(f"{x} + {y} = {z}")
    print(f"Score: {score}")

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
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
        z = x + y
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
        z = x + y
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
        z = x + y
    return x,y,z



if __name__ == "__main__":
    main()