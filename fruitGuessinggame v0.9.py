#fruitGuessinggame
#Nathaniel Fu
#Version 0.9

import time
import sqlite3
import random

def randomFruit(): #This function is connected to a database in order to randomly select a fruit from a database which contains a list of fruit.
    with sqlite3.connect("FruitDatabase(GitHub)/fruits.db") as db: #Here is the code that connects my database to randomFruit function.
        cursor = db.cursor()
        cursor.execute("select FruitName from fruits")
        fruitList = cursor.fetchall()
        selectFruit = random.choice(fruitList) #A fruit is randomly selected from the database.
        result = True
        while result == True:
            result = jumbleFruit(selectFruit) #Send selectFruit to jumbleFruit function.
            selectFruit = random.choice(fruitList) #A fruit is randomly selected from the database.
            if result == False:
                userOption = input("Please select an option:\n"
                                   "1. Play Again\n"
                                   "2. Quit\n")
                while userOption != '1' and userOption != '2':
                    print ("Invalid entry\n")
                    userOption = input("Please select an option:\n"
                                   "1. Play Again\n"
                                   "2. Quit\n")
                if userOption == '1':
                    result = True
        print ("Good-Bye")
    
def jumbleFruit(selectFruit): #This function jumbles a string and displays it for the player to guess the jumbled word.
    jumbledFruit = str(''.join(selectFruit)) #Change selectFruit variable into string type.
    jumbledFruit = list(jumbledFruit) #Then change selectFruit into a list type. This enables random.shuffle module to shuffle the word.
    random.shuffle(jumbledFruit) #Word gets shuffled here using random.shuffle module.
    print("The jumbled fruit is... ")
    print(''.join(jumbledFruit)) #Print jumbledFruit
    userGuess = input("Enter your guess: ") #The player is asked to enter a guess.
    counter = 4
    while counter > 1:
        if userGuess == str(''.join(selectFruit)): #If userGuess is the same as selectFruit, print "Good Job."
            print("Good Job. Here comes the next fruit.")
            return True
        elif userGuess != str(''.join(selectFruit)): #Else/if userGuess is not the same as selectFruit, let the player try again.
            counter = counter -1
            userGuess = input("You have {0} more guesses left. Please guess again: ".format(counter)) 
        if counter == 1:
            userGuess = input("You are out of guesses. Make a final guess: ")
            if userGuess == str(''.join(selectFruit)):
                print("Good job.")
                return True
            else:
                print("Bad luck")
                return False

def fruitGuessinggame(): #This function requests for the players name.
    print("Welcome to fruit guessing game.\n") #Welcomes the user to fruit guessing game.
    print("How To Play: Unscramble the letters to make a word.")
    print("NOTE: You have 4 guesses. If you get the first guess wrong a guess is taken off you.\n"
        "For every jumbled fruit you will start with 4 guesses.\n"
        "If you guess right, you move onto the next jumbled fruit.\n") #Instructions of how to play fruit guessing game.
    userName = input("Enter player name: ") #Requests for a name.
    while True:
        if any(char.isdigit() for char in userName) == True:
            userName = input("Enter your name again: ") #Ask for their name again because they might have entered integers.
        elif len(userName) > 15 or len(userName)  < 3: 
            userName = input("It's too long or too short. Please try again: ") #Asks for the player's name again because it contains over 15 characters or less than 3 characters.
        else:
            print("Hello, nice to meet you {0}".format(userName)) #Else, print userName.
            break #Break out of while loop
    randomFruit() #Go to randomFruit function.
        
fruitGuessinggame()


