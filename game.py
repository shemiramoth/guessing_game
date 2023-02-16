#this program demonstrates a guessing game
from random import randint

#1. get username
username = input("Enter your name: ")
print("Hello "+ username + "!")


#2. generate a random number
number= randint(10,50)
 
#3. using a while loop, check if user input is equal to generated number
counter = 0
while counter < 5:
    user_number = eval(input("Enter a random number to win: "))

