"""Component 3 (question_generator) v1
Generates random choice of tokens in random order and asks a question to the user"""

import random

tokens = ["tahi", "rua"]


NUMBER_OF_QUESTIONS = 2
questions = NUMBER_OF_QUESTIONS
STARTING_SCORE = 0
score = STARTING_SCORE
token = random.choice(tokens)

# Testing loop


def question_check():
    for item in range(1):
        random.choice(tokens)
        while questions != 0:
            return item

# Main routine

answer = input(f"What number is {token}? ")
if answer == token:
    print("Well done that was correct")
elif answer != token:
    print("That was incorrect, unlucky")
