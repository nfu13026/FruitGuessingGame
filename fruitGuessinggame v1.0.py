#fruitGuessinggame
#Nathaniel Fu
#Version 0.9

import sqlite3
import random

""" 
#This function is connected to a database in order to randomly select a fruit from a database which contains a list of fruit.
"""
def randomFruit():
    with sqlite3.connect("FruitDatabase(GitHub)/fruits.db") as db: #Here is the code that connects my database to randomFruit function.
        cursor = db.cursor()
        cursor.execute("select FruitName from fruits")
        fruitList = cursor.fetchall()
        selectFruit = random.choice(fruitList) #A fruit is randomly selected from the database.
        result = True #This variable is set to True so that it can be used in the while loop to check if they meet the conditions for the next jumbledFruit.
        while result == True:#While result is True check that if the player meets all the conditions below. If result is True, randomly select a fruit and pass it to def jumbleFruit.
            result = jumbleFruit(selectFruit) #Send selectFruit to jumbleFruit function.
            selectFruit = random.choice(fruitList) #A fruit is randomly selected from the database.
            if result == False:#If result is False, give them options to select.
                userOption = input("Please select an option:\n"#Request for userOption.
                                   "1. Play Again\n"
                                   "2. Quit\n")
                while userOption != '1' and userOption != '2':#While userOption is not equal to 1 and 2, print Invalid entry. Then, make them select again.
                    print ("Invalid entry\n")
                    userOption = input("Please select an option:\n"#Request for userOption.
                                   "1. Play Again\n"
                                   "2. Quit\n")
                if userOption == '1':#If userOption equal to 1 then result is True so randomly select another fruit.
                    result = True
        print ("Good-Bye")#Otherwise, print "Good-Bye".

"""
#This function jumbles a string, displays it for the player to guess the jumbled word and keeps track of guesses used. When the player has uses all guesses let them choose an option.
"""
def jumbleFruit(selectFruit):
    jumbledFruit = str(''.join(selectFruit)) #Change selectFruit variable into string type.
    jumbledFruit = list(jumbledFruit) #Then change selectFruit into a list type. This enables random.shuffle module to shuffle the word.
    random.shuffle(jumbledFruit) #Word gets shuffled here using random.shuffle module.
    print("The jumbled fruit is... ")
    print(''.join(jumbledFruit)) #Print jumbledFruit
    userGuess = input("\nEnter your guess: ") #The player is asked to enter a guess.
    counter = 5 #Set counter to 5 because computers awlays start on zero. This variable shows many guesses the player has left.
    while counter > 0:
        counter = counter -1 #Take away one guess for each guess is incorrect.
        if userGuess == str(''.join(selectFruit)): #If userGuess is the same as selectFruit, print "Good Job."
            print("Good Job. Here comes the next fruit.\n")
            return True #Return True if the player passess the condition by guessing the jumbledFruit right then go to the while loop in def randomFruit to select a random fruit.        
        elif counter == 0:#If counter is equal to one. Make them enter a final guess.
            print("Guesses left: {0}".format(counter))
            userGuess = input("You are out of guesses. Make a final guess: ")#Enter final guess.
            if userGuess == str(''.join(selectFruit)):#If their final guess is correct, print good job and go to the next jumbled fruit.
                print("Good job. Here comes the next fruit.\n")
                return True #Return True if they guess correctly then go to the while loop in def randomFruit to select a random fruit
            else:#Otherwise if their guess is incorrect, display Bad Luck.
                print("Bad luck\n")
                return False#If they meet the conditions of the else statement, return False to the while loop in def randomFruit and give them options to select.        
        elif userGuess != str(''.join(selectFruit)): #Else/if userGuess is not the same as selectFruit, let the player try again.
            print("Guesses left: {0}".format(counter))
            userGuess = input("You have {0} more guesses left. Please guess again: ".format(counter)) #Display the number of guesses if the player guess is incorrect.
            
"""
This function requests for the player's name. If the player's name contains integers make them enter their name again or if the player's name is too short or too long make them enter their name again.
"""
def fruitGuessinggame():
    print("Welcome to fruit guessing game.\n") #Welcomes the user to fruit guessing game.
    print("How To Play: Unscramble the letters to make a word.")
    print("NOTE: You have 4 guesses. If you get the first guess wrong a guess is taken off you.\n"
        "For every jumbled fruit you will start with 4 guesses.\n"
        "If you guess right, you move onto the next jumbled fruit.\n"
        "If you have used up all your guesses you will be asked to select an option.\n") #Instructions of how to play fruit guessing game.
    userName = input("Enter player name: ") #Requests for a name.
    while True:
        if any(char.isdigit() for char in userName) == True:
            userName = input("Enter your name again: ") #Ask for their name again because they might have entered integers.
        elif len(userName) < 3: #If the player enters less than 3 characters make them enter their name again.
            userName = input("It's too short. Please try again: ")
        elif len(userName) > 15: #If the player enters more than 15 characters make them enter their name again.
            userName = input("It's too long. Please try again: ")
        else:
            print("Hello, nice to meet you {0}.\n".format(userName)) #Else, print userName.
            break #Break out of while loop
    randomFruit() #Go to randomFruit function.
        
fruitGuessinggame()


