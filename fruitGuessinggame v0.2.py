#fruitGuessinggame
#Nathaniel Fu
#Version 0.2

import sqlite3

def randomFuit(): #This function fetches a list of fruit from a database which was created using SQL.
    with sqlite3.connect("fruits.db") as db: 
        cursor = db.cursor()
        cursor.execute("select FruitName from fruits") #Making a query calling for the list of fruits from my database called fruits.
        selectedFruit = cursor.fetchall()
        print(selectedFruit) #Print selected fruit.

def fruitGuessinggame():
    print("Welcome to fruit guessing game.") #Greets the user.
    print("")
    userName = input("Enter player name: ") #Requests for user's name.
    while True:
        if any(char.isdigit() for char in userName) == True: #While loop. If the user inputs an integer let them type their name again until the user inputs a string.
            userName = input("Enter your name again: ")
        elif len(userName) > 15:
            userName = input("Please shorten your name: ") #If userName is longer than 15 characters let the player to enter their name again.
        else:
            print("Hello, nice to meet you {0}".format(userName)) #Else, print userName.
            break
    #while userGuess > 5:
        #userGuess = input("Enter a guess: ")
        #if userGuess != selectedFruit:
            #print("Good Job")
        #else:
            #userGuess = input("Please try again: ")
fruitGuessinggame()



