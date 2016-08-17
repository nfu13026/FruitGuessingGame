#fruitGuessinggame
#Nathaniel Fu
#Version 0.5

import time
import sqlite3
import random
from random import shuffle

def randomFruit():  #This function fetches a list of fruit from a database which was created using SQL.
    with sqlite3.connect("FruitDatabase/fruits.db") as db: #Here is the code that connects my database to randomFruit function. 
        cursor = db.cursor()
        cursor.execute("select FruitName from fruits") #Making a query calling for the list of fruits from my database called fruits.
        fruitList = cursor.fetchall()
        print()
        selectFruit = random.choice(fruitList) #A fruit is randomly selected from the database.
        print(jumbleFruit(selectFruit))
    
def jumbleFruit(word):
    word = ""
    while word:
        position = random.range(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
    
def fruitGuessinggame(): 
    print("Welcome to fruit guessing game.") #Welcomes the user to fruit guessing game.
    print("")
    print("How To Play: Unscramble the letters to make a word.") #Instructions of how to play fruit guessing game.
    time.sleep(2)
    userName = input("Enter player name: ") #Requests for a name.
    while True: 
        if any(char.isdigit() for char in userName) == True: #This code checks for any integers within the userName variable. This restricts the player to enter string only.
            userName = input("Enter your name again: ") #Asks for their name again because the user might have entered integers.
        if len(userName) > 15: #If userName has more than 15 characters ask the player to enter a name again.
            userName = input("Please shorten your name: ") #Request for their name again because the user has passed the condition.
        else:
            print("Hello, nice to meet you {0}".format(userName)) #Else, print userName.
            break 
    randomFruit()

fruitGuessinggame()


