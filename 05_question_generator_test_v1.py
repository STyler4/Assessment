"""Component 3 (question_generator) v1
Generates random choice of tokens in random order and asks a question to the user"""

import random

tokens = ["tahi", "rua"]
token_2 = []

for i in tokens:
    if i not in token_2:
        token_2.append(i)


NUMBER_OF_QUESTIONS = 30
questions = NUMBER_OF_QUESTIONS
STARTING_SCORE = 0
score = STARTING_SCORE


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
            else:
                questions -= 1
                print("That was incorrect unlucky")
        elif token == "rua":
            answer = input("What number is rua? ")
            if answer == "2":
                questions -= 1
                score += 1
                print("Well done that is correct")
            else:
                questions -= 1
                print("That was incorrect unlucky")


# Main routine
    print(f"You have a score of {score} at the moment"
          f" and have {questions} questions left")
