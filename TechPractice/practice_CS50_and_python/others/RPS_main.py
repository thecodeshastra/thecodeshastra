import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == "S":
        if you == "P":
            return False
        elif you == "R":
            return True
    elif comp == "P":
        if you == "R":
            return False
        elif you == "S":
            return True
    elif comp == "R":
        if you == "S":
            return False
        elif you == "P":
            return True

print("Comp turn Rock(R), Paper(p), Scissor(S)? : ")
rand = random.randint(1,3)
if rand == 1:
    comp = "R"
elif rand == 2:
    comp = "P"
elif rand == 3:
    comp = "S"

you =input("Your turn Rock(R), Paper(p), Scissor(S)? : ")
a = gameWin(comp, you)
print(f"Computer chosen {comp}")
print(f"You chosen {you}")

if a == None:
    print("This is a tie!")
elif a:
    print("You win!")
else:
    print("You lose!")