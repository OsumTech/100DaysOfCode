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

#Step2


#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.



display_word =[]

for letter in chosen_word:
    display_word.append("_")



#step3

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.


dash = "_"
while dash in display_word:
    guess = input("Guess a letter: ").lower()
    i=0
    for letter in chosen_word:
     if letter == guess:
        display_word[i] = guess
     i += 1
    print(display_word)   
else:
    print("Congratulations!!! You Have Won!")

