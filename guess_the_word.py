import random

words = ['cat', 'computer', 'coffee']
man = ["________ \n| \n| \n| \n| \n| \n| \n|____________",
       "________ \n|      | \n| \n| \n| \n| \n| \n|____________",
       "________ \n|      | \n|      O \n| \n| \n| \n| \n|____________",
       "________ \n|      | \n|      O \n|      | \n| \n| \n| \n|____________",
       "________ \n|      | \n|      O \n|      | \n|      | \n| \n| \n|____________",
       "________ \n|      | \n|      O \n|     /| \n|      | \n| \n| \n|____________",
       "________ \n|      | \n|      O \n|     /| \n|    / | \n| \n| \n|____________",
       "________ \n|      | \n|      O \n|     /|\\ \n|    / | \n| \n| \n|____________",
       "________ \n|      | \n|      O \n|     /|\\ \n|    / | \\ \n| \n| \n|____________",
       "________ \n|      | \n|      O \n|     /|\\ \n|    / | \\ \n|     / \n| \n|____________",
       "________ \n|      | \n|      O \n|     /|\\ \n|    / | \\ \n|     / \n|    / \n|____________",
       "________ \n|      | \n|      O \n|     /|\\ \n|    / | \\ \n|     / \\ \n|    / \n|____________",
       "________ \n|      | \n|      O \n|     /|\\ \n|    / | \\ \n|     / \\ \n|    /   \\ \n|____________"]

word = random.choice(words)
guesses = ""
wrong_guesses = ""
turns = 12

print("Guess the word")
while turns > 0:
    print("___________________________________________________________________\n")
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    print("") # new line
    if failed == 0:
        print("You Win!")
        print(f"The word is: {word}")
        break
    print()
    while True:
        guess = input("Input letter: ")

        if len(guess) == 1 and guess.isalpha(): # check for more than one character and not letter character
            guess = guess.lower() # make the letter lowercase if it is uppercase
            break
        else:
            print("Enter a single letter (a-z).")
            continue
    guesses += guess
    if guess not in word: #checks if the letter entered is part of a word
        turns -= 1
        print(f"Wrong! You have {turns} more guesses")
        wrong_guesses += guess + " "
        if turns == 0:
            print("You Loose!")
    print(f"Wrong letters are: {wrong_guesses}")
    print(man[12 - turns])