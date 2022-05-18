"""Component 3 (question_generator) v1
Generates random choice of tokens in random order and asks a question to the user"""

import random

tokens = ["tahi", "rua", "toru", "whā", "rima", "ono",
          "whitu", "waru", "iwa", "tekau", "tekau mā tahi", "tekau mā rua",
          "tekau mā toru", "tekau mā whā", "tekau mā rima", "tekau mā ono",
          "tekau mā whitu", "tekau mā waru", "tekau mā iwa", "rua tekau",
          "rua tekau mā tahi", "rua tekau mā rua", "rua tekau mā toru",
          "rua tekau mā whā", "rua tekau mā rima", "rua tekau mā ono",
          "rua tekau mā whitu", "rua tekau mā waru", "rua tekau mā iwa", "toru tekau"]

NUMBER_OF_QUESTIONS = 30
questions = NUMBER_OF_QUESTIONS
STARTING_SCORE = 0
score = STARTING_SCORE
token = random.choice(tokens)

# Testing loop

while True:
    for item in range(1):
        token = random.choice(tokens)
    if token == "tahi":
        answer = input("What number is tahi? ")
        if answer == "1":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "rua":
        answer = input("What number is rua? ")
        if answer == "2":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "toru":
        answer = input("What number is toru? ")
        if answer == "3":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "whā":
        answer = input("What number is whā? ")
        if answer == "4":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "rima":
        answer = input("What number is rima? ")
        if answer == "5":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "ono":
        answer = input("What number is ono? ")
        if answer == "6":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "whitu":
        answer = input("What number is whitu? ")
        if answer == "7":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "waru":
        answer = input("What number is waru? ")
        if answer == "8":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "iwa":
        answer = input(f"What number is iwa? ")
        if answer == "9":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "tekau":
        answer = input("What number is tekau? ")
        if answer == "10":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "tekau mā tahi":
        answer = (input("What number is tekau mā tahi? "))
        if answer == "11":
            print("Well done that is correct")
            questions -= 1
        elif answer == "":
            print("Invalid please try again")
        else:
            score -= 1
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "tekau mā rua":
        answer = (input("What number is tekau mā rua? "))
        if answer == "12":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "tekau mā toru":
        answer = (input("What number is tekau mā toru? "))
        if answer == "13":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "tekau mā whā":
        answer = (input("What number is tekau mā whā? "))
        if answer == "14":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "tekau mā rima":
        answer = (input("What number is tekau mā rima? "))
        if answer == "15":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "tekau mā ono":
        answer = (input("What number is tekau mā ono? "))
        if answer == "16":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "tekau mā whitu":
        answer = (input("What number is tekau mā whitu? "))
        if answer == "17":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "tekau mā waru":
        answer = (input("What number is tekau mā waru? "))
        if answer == "18":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "tekau mā iwa":
        answer = (input("What number is tekau mā iwa? "))
        if answer == "19":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "rua tekau":
        answer = (input("What number is rua tekau? "))
        if answer == "20":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "rua tekau mā tahi":
        answer = (input("What number is rau tekau mā tahi? "))
        if answer == "21":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "rua tekau mā rua":
        answer = (input("What number is rau tekau mā rua? "))
        if answer == "22":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "rua tekau mā toru":
        answer = (input("What number is rua tekau mā toru? "))
        if answer == "23":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "rua tekau mā whā":
        answer = (input("What number is rua tekau mā whā? "))
        if answer == "24":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "rua tekau mā rima":
        answer = (input("What number is rua tekau mā rima? "))
        if answer == "25":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "rua tekau mā ono":
        answer = (input("What number is rua tekau mā ono? "))
        if answer == "26":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "rua tekau mā whitu":
        answer = (input("What number is tekau mā whitu? "))
        if answer == "27":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "rua tekau mā waru":
        answer = (input("What number is tekau mā waru? "))
        if answer == "28":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "rua tekau mā iwa":
        answer = (input("What number is tekau mā iwa? "))
        if answer == "29":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")
    elif token == "toru tekau":
        answer = (input("What number is toru tekau? "))
        if answer == "30":
            questions -= 1
            score += 1
            print("Well done that is correct")
        elif answer == "":
            print("Invalid please try again")
        else:
            questions -= 1
            print("That was incorrect unlucky")

# Main routine
    print(f"You have a score of {score} at the moment"
          f" and {questions} questions left")
