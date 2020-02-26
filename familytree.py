#!/usr/bin/env python3.8

class Family:
    Nigerian = True
    def location(self):
        print("London")

class mum(Family):
    age = 50
    name = "Adeola"
    children = 0

    def __init__(self):
        self.age
        self.name
        self.children
    
    def children(self):
        self.children = "has 4 children"

    def name(self):
        self.name = "name is Adeola"

    def age(self):
        self.age = "Age is 50"

        

fashoro = mum()
fashoro.location()
fashoro.name()
print(fashoro.name)
fashoro.children()
print(fashoro.children)

    