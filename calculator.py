#!/usr/bin/env python3.8

#simple calculator
def add (x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

x = int(input("enter value for x: "))
y = int(input("enter value for y: "))

intro = input("What will you like to use? ")

if intro == '+':
    print(x + y)

elif intro == '-':
    print(x - y)

elif intro == '*':
    print(x * y)

elif intro == '/':
    print(x / y)

else:
    print("symbol is not recognised")


