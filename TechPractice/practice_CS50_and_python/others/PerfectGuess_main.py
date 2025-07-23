import random
RandGuess = random.randint(1,100)
print(RandGuess)
guesses = 0
UserGuess = None
while RandGuess != UserGuess:
    UserGuess = int(input("Enter your guess: "))
    guesses += 1
    if RandGuess == UserGuess:
        print("You gussed it correct")
    else:
        if RandGuess<UserGuess:
            print("You guessed it incorrect enter a smaller number")
        else:
            print("You guessed it incorrect enter a larger number")

print(f"User has tried {guesses} time to reach correct answer")
print(f"No of guesses is = {guesses}")

with open("C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\highscore1.txt", "r") as f:
        highscore = int(f.read())
if highscore>guesses:
    print("You have broken the highscore!")
    with open("C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\highscore1.txt", "w") as f:
            f.write(str(guesses))