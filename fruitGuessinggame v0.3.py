#fruitGuessinggame
#Nathaniel Fu
#Version 0.3

import sqlite3
import random

def randomFruit(): #This function fetches a list of fruit from a database which was created using SQL.
    with sqlite3.connect("FruitDatabase/fruits.db") as db: #Connected a database file from my H: drive.
        cursor = db.cursor()
        cursor.execute("select FruitName from fruits") #Making a query calling for the list of fruits from my database called fruits.
        fruitList = cursor.fetchall()
        selectFruit = random.choice(fruitList)
        print()
        jumbleFruit(selectFruit)
        #print(selectFruit)
        
def jumbleFruit(selectFruit): #Function is still in development.
    x = selectFruit
    random.shuffle(x)
    y = ' '.join(x)
    print(y)


def fruitGuessinggame():
    print("Welcome to fruit guessing game.") #Welcomes the user to the game.
    print("")
    userName = input("Enter player name: ") #Requests for a name.
    #while True:
    if any(char.isdigit() for char in userName) == True: #While loop. If the user inputs integer let them type their name again until the name is all string. 
        userName = input("Enter your name again: ")
    elif len(userName) > 15:
        userName = input("Please shorten your name: ") #If userName is longer than 15 characters let the player to enter their name again.
    else:
        print("Hello, nice to meet you {0}".format(userName)) #Else, print userName.
        randomFruit()
            
fruitGuessinggame()


