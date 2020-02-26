#!/usr/bin/env python3

# rock paper scissors game
import random
game = True

rps = ["rock", "paper", "scissors"]

rock_counter =0
paper_counter = 0
scissors_counter = 0

def better_decision ():
    max_counter = max(rock_counter, paper_counter, scissors_counter)
    if rock_counter == max_counter:
        return 1
    if paper_counter == max_counter:
        return 2
    if scissors_counter == max_counter:
        return 0
    else:
        return random.randint(0,2)

while game:

        computer_decision = better_decision()

        player_decision = int(input("select 0 for rock, 1 for paper, or 2 for scissors"))

        if player_decision == computer_decision:
            if player_decision == 0:
                rock_counter +=1
            if player_decision == 1:
                player_counter +=1
            if player_decision == 1:
                paper_counter +=1
            if player_decision == 2:
                paper_counter +=1
            print("tie!" + " you selected " + rps[player_decision] + ", computer selcected " + rps[player_decision])
        elif player_decision == 0 and computer_decision == 1:
            rock_counter +=1
            print("you lose" + " you selected " + rps[player_decision] + ", computer selcected " + rps[player_decision])
        elif player_decision == 1 and computer_decision == 2:
            paper_counter +=1
            print("you lose" + " you selected " + rps[player_decision] + ", computer selcected " + rps[player_decision])
        elif player_decision == 2 and computer_decision == 0:
            scissors_counter +=1
            print("you lose" + " you selected " + rps[player_decision] + ", computer selcected " + rps[player_decision])
        else:
            print("you win" + " you selected " + rps[player_decision] + ", computer selcected " + rps[player_decision])

        player_session = input("do you want to continu? y/n: ")

        if player_session.lower() == "n":
            game = False
        elif player_session.lower() == "y":
            pass
        else:
            if player_decision == 0:
                rock_counter +=1
            if player_decision == 1:
                player_counter +=1
            if player_decision == 1:
                paper_counter +=1
            if player_decision == 2:
                paper_counter +=1
            print("please enter a valid input")

