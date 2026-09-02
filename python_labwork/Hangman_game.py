import random

words = ['python', 'Java', 'Javascript', 'Csharp', 'Dotnet']


word = random.choice(words)

guessed_word = ["_"] * len(word) 

attempts = 6

guessed_letters = []

print("Welcome to Hangman Game!")

while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Attempts Left:", attempts)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        print("Wrong Guess!")
        attempts -= 1

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)



"""
import random                  # Import random module

words = [...]                  # List

word = random.choice(words)    # Select random item from list

guessed_word = ["_"] * len(word)   # Create list of underscores

attempts = 6                   # Variable Assignment

guessed_letters = []           # Empty List

while attempts > 0 and "_" in guessed_word:
                               # While Loop with condition

print()                        # Output Function

input()                        # Take user input

.lower()                       # Convert text to lowercase

if guess in guessed_letters:   # Membership Operator (in)

continue                       # Skip current loop iteration

guessed_letters.append(guess)  # Add item to list

if guess in word:              # If Statement

else:                          # Else Statement

for i in range(len(word)):     # For Loop

range()                        # Generate sequence of numbers

len(word)                      # Length Function

word[i]                        # Access character by index

guessed_word[i] = guess        # Update List Element

attempts -= 1                  # Decrement Operator

" ".join(guessed_word)         # Join list elements into string

"_" not in guessed_word        # Membership Test (not in)

random.choice(words)           # Random Selection Function

==                             # Equality Operator

>                              # Greater Than Operator

and                            # Logical AND Operator

=                              # Assignment Operator


()                             # Function Call

:                              # Start of code block

"""
