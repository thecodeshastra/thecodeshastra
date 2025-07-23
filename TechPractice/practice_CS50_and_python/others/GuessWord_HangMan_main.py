import random

def hangMan():
    word = random.choice(["ramji", "hanumanji", "laxmanji", "bharatji", "shtruganji", "shugrivji", "angadji", "kesriji"])
    # print(word)
    validity = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guessWord = ''

    while len(word) > 0:
        main = ""

        # if guess word corects
        for l in word:
            if l in guessWord:
                main = main + l
            else:
                main = main + "_" + " "

        # If guess is done
        if main == word:
            print(main)
            print("You won the game and man is saved")
            break

        #Asks user to guess a word
        print("Guess The Word :- "+ main)
        guess = input()
        
        # check guessed word validity
        if guess in validity:
            guessWord = guessWord + guess
        else:
            print("Enter a valid word from a to z")
        
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\     ")
                print("    / \     ")
                break



name = input("Enter You Name :- ")
print("Welcome, " + str(name))
print("------------------------")
print("Guess the dashed word in less than 10 attempts")
print("Hint :- Its gods name from Ramayana with surfix 'ji'")
hangMan()
print()
