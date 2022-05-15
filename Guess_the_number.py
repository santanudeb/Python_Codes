''' Guess the number '''

from enum import Flag
import random

Flag = False
high = int(input("Enter high : "))
low = int(input("Enter low : "))

magicNumber = random.randint(low, high)

while Flag != True :
    guessedNumber = int(input(f"Guess a number : "))
    if (guessedNumber > magicNumber) :
        print("You are too high")
    elif (guessedNumber < magicNumber) :
        print("You are too low")
    else :
        print("accurate") 
        Flag = True  