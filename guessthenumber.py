#!/usr/bin/env python3.8

#guess the number game

import random

number = random.randint(1, 20)

print("guess the number!")

guess = int(input("take a random guess "))

if guess < number:
    print("Incorrect, your guess is too low")

elif guess > number:
    print("Incorrect, your guess is too high"
    
else:
    print("You guessed correctly!")




