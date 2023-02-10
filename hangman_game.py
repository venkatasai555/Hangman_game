# Modules
import random
import time
import os
clear = lambda: os.system('cls')

# Variables from extras.py
from About import line
from About import title_screen
from About import game_rules
from About import you_win
from About import you_lose
from About import hangman_arts
from About import list_of_editions
from About import dialogues_start
from About import positive_dialogues
from About import negative_dialogues

# Functions
def main_menu():
    # Main Menu
    print(line)
    print(title_screen)
    print(line)
    time.sleep(1)
    play = input("Press ENTER to play!: ")
    print()
    
def ask_for_game_rule():
    # Game Rules
    yes_no_game_rules = input("Do you want to read the game rules? (y/n): ")
    print()
    clear()

    if yes_no_game_rules.strip().lower() == "y":
        print(line)
        print(game_rules)
        
def select_edition():
    # Editions and selecting editions
    incorrect = True
    while incorrect:
        id_of_edition_to_play = input("What edition do you want to play? {}: ".format([str(i+1) + " - " + list_of_editions[i][1] for i in range(len(list_of_editions))]))
        print()

        list_of_number_str = []
        for i in range(len(list_of_editions)):
            list_of_number_str.append(str(i+1))

        if id_of_edition_to_play in list_of_number_str:
            edition_to_play = list_of_editions[int(id_of_edition_to_play) - 1][0]
            name_of_edition_to_play = list_of_editions[int(id_of_edition_to_play) - 1][1]
            incorrect = False
            return edition_to_play, name_of_edition_to_play
        else:
            print("You have to enter a number from {first} to {second}.".format(first=1, second=len(list_of_editions)))       
            
def play_game():
    # Dialogues
    random_index1 = random.randint(0, len(dialogues_start) - 1)
    dialogue = dialogues_start[random_index1]

    # Story
    hangman = input("Name your hangman: ")
    gender = input("Gender of your hangman [him/her/them/hir]: ")
    print()
    time.sleep(1)
    print("Oh no! " + hangman + " will be hanged!")
    time.sleep(1)
    print("Guess the word to release " + gender + ".")
    time.sleep(1)
    print()
    clear()
    
    # Randomly selecting word
    random_index4 = random.randint(0, len(edition_to_play) - 1)
    word = edition_to_play[random_index4]
    
    temporary_string = ""
    for letter in word:
        if letter != " ":
            temporary_string += "-"
        else:
            temporary_string += letter

    # Solo game main algorithm
    lives = len(hangman_arts) - 1
    lives_string = "Lives: {}".format(lives)

    print(line)
    print("Let's start the game!")
    print()
    time.sleep(1) 
    print(lives_string)
    print("Edition: " + name_of_edition_to_play)
    print("Word: " + temporary_string)
    print(hangman_arts[len(hangman_arts) - lives - 1])
    print(hangman + ": " + dialogue)
    print()

    guess_word = ""
    letters_used = ""

    # Loop until we win or lose
    while temporary_string != word and lives > 0 and guess_word != word:
        random_index2 = random.randint(0, len(negative_dialogues) - 1)
        negative_dialogue = negative_dialogues[random_index2]

        random_index3 = random.randint(0, len(positive_dialogues) - 1)
        positive_dialogue = positive_dialogues[random_index3]

        guess_raw = input("Guess letter: ")
        guess = guess_raw.strip().lower()

        while not guess in "abcdefghijklmnopqrstuvwxyz":
            print("Guess is not a letter!")
            print()
            time.sleep(1)
            guess_raw = input("Guess letter: ")
            guess = guess_raw.strip().lower()

        while guess in letters_used and guess != "":
            print("Letter is already used.")
            print()
            time.sleep(1)
            guess_raw = input("Guess letter: ")
            guess = guess_raw.strip().lower()

        guess_word_raw = input("Guess word (press ENTER if you don't have any guess): ")
        guess_word = guess_word_raw.strip().lower()
        print()
        clear()

        letters_used += guess + " "
        print(line)
        
        new_temporary_string = temporary_string
        lives_string = "Lives: {}".format(lives)

        if (guess in word and guess != "") and guess_word != word:
            for i in range(len(word)):
                if word[i] == guess:
                    temporary_string = new_temporary_string[:i] + word[i] + new_temporary_string[i+1:]
                    
                new_temporary_string = temporary_string

            if temporary_string != word:
                print("Nice work!")
                print()
                time.sleep(1)
                print("Letter used: " + letters_used)
                print(lives_string)
                print("Edition: " + name_of_edition_to_play)
                print("Word: " + new_temporary_string)
                print(hangman_arts[len(hangman_arts) - lives - 1])
                print(hangman + ": " + positive_dialogue)
                print() 

        elif guess_word != word:
            lives = lives - 1
            lives_string = "Lives: {}".format(lives)
            print("The letter is not in the word.")
            print()
            time.sleep(1)
            print("Letter used: " + letters_used)
            print(lives_string)

            print("Edition: " + name_of_edition_to_play)
            print("Word: " + new_temporary_string)

            print(hangman_arts[len(hangman_arts) - lives - 1])
            
            if lives > 0:
                print(hangman + ": " + negative_dialogue)
            else:
                print(hangman + ": Noooooooo-")
            print()

        temporary_string = new_temporary_string

    if temporary_string == word or guess_word == word:
        print(you_win)
        time.sleep(1)
        print("Letter used: " + letters_used)
        print("The word is " + word + ".")
        print(hangman + ": Thank you!")
        print()
    else:
        print(you_lose)
        time.sleep(1)
        print("Letter used: " + letters_used)
        print("The word is " + word + ".")
        print()

# Play game
clear()
play = True
game_status = True

# While loop for the status of the game
while game_status:
    main_menu()
    clear()
    print(line)
    
    ask_for_game_rule()
    print(line)
    

    # Gameplay
    while play:  
        edition_to_play, name_of_edition_to_play = select_edition()
        clear()
        print(line)
        
        play_game()
        print(line)

        # Option to terminate gameplay
        again = input("Play again? (y/n): ")
        print()
        clear()
        print(line)

        if again.strip().lower() == "n":
            play = False

    # Option to terminate the status of the game
    return_to_menu = input("Return to main menu? (y/n): ")
    
    if return_to_menu.strip().lower() == "n":
        game_status = False
    else:
        play = True
        game_status = True

    print()
    clear()