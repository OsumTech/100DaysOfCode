#Step 1 

word_list = ["aardvark", "baboon", "camel", "happy", ]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

import random

chosen_word = random.choice(word_list)
print (chosen_word)

#Step2


#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

guess = input("Guess a letter: ").lower()

display_word =[]

for letter in chosen_word:
    display_word.append("_")
    
print (display_word)

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
i = 0
for letter in chosen_word:
    i += i
    if letter == guess:
        display_word[i] = guess
        print(display_word)

    else:
        print("Wrong")
    print(i)


#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

