#fruitGuessinggame
#Nathaniel Fu
#Version 0.4

import sqlite3
import random
from random import shuffle

def randomFruit():  #This function fetches a list of fruit from a database which was created using SQL.
    with sqlite3.connect("FruitDatabase/fruits.db") as db:#Connected a database file from my H: drive.
        cursor = db.cursor()
        cursor.execute("select FruitName from fruits") #Making a query calling for the list of fruits from my database called fruits.
        fruitList = cursor.fetchall()
        selectFruit = random.choice(fruitList)
        print()
        jumbleFruit(selectFruit)
        #print(selectFruit)
        
def jumbleFruit(selectFruit):
    x = selectFruit
    random.shuffle(x)
    y = "".join(x)
    print(y)


def fruitGuessinggame():
    print("Welcome to fruit guessing game.") #Welcomes the user to the game.
    print("")
    userName = input("Enter player name: ") #Requests for a name.
    while True: #This  while loop is not working in this version.
        if any(char.isdigit() for char in userName) == True:
            userName = input("Enter your name again: ") #Ask for their name again because they might have entered integers.
        elif len(userName) > 15:
            userName = input("Please shorten your name: ") #Ask for their name again because it is too long.
        else:
            print("Hello, nice to meet you {0}".format(userName)) #Else, print name.
        break
    randomFruit()
            
fruitGuessinggame()


