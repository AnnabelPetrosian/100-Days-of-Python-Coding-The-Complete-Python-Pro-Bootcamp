#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

chosen_word = random.choice(word_list)


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess_letter = input("Guess a letter: ").lower()


#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
    if letter == guess_letter:
        print("Correct guess. ")
    else:
        print("Wrong guess. ")