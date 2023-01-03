#Step 1 

word_list = ["aardvark", "baboon", "camel", "happy", ]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list)
print (chosen_word)


display_word =[]

for letter in chosen_word:
    display_word.append("_")


lives = 6
dash = "_"
while dash in display_word:
    guess = input("Guess a letter: ").lower()
    i=0
    for letter in chosen_word:
     if letter == guess:
        display_word[i] = guess
     i += 1
    print(f"{' '.join(display_word)}")
else:
    print("Congratulations!!! You Have Won!")

#step4
#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
#TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
