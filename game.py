#this program demonstrates a guessing game
from random import randint

#1. get username
username = input("Enter your name: ")
print("Hello "+ username + "!")


#2. generate a random number
random_number= randint(10,50)
 
#3. using a while loop, check if user input is equal to generated number
counter = 0
while counter < 5:
    user_number = eval(input("Enter a random number to win: "))
    counter = counter+1 #also conter += 1


    if user_number<random_number:
        print("Your guess is too low, try again: ")
    elif user_number> random_number:
        print("Your guess is too high try agan: ")
    elif user_number==random_number:
        break



if user_number == random_number:
    print("Congratulations You Have WON!!")
else:
    print("Are you dumb..Game Over!! The correct number is ")
    print(random_number)

