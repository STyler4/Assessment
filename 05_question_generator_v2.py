"""Component 3 (question_generator) v1
Generates random choice of tokens in random order and asks the question to the user"""

import random

tokens = ["tahi", "rua", "toru", "whā", "rima", "ono",
          "whitu", "waru", "iwa", "tekau", "tekau mā tahi", "tekau mā rua",
          "tekau mā toru", "tekau mā whā", "tekau mā rima", "tekau mā ono",
          "tekau mā whitu", "tekau mā waru", "tekau mā iwa", "rua tekau",
          "rua tekau mā tahi", "rua tekau mā rua", "rua tekau mā toru",
          "rua tekau mā whā", "rua tekau mā rima", "rua tekau mā ono",
          "rua tekau mā whitu", "rua tekau mā waru", "rua tekau mā iwa", "toru tekau"]

# Testing loop
for item in range(1):
    token = random.choice(tokens)
    if token == "tahi":
        print("What number is tahi? ")
    elif token == "rua":
        print("What number is rua")
    elif token == "toru":
        print("What number is toru")
    elif token == "whā":
        print("What number is whā")
    elif token == "rima":
        print("What number is rima")
    elif token == "ono":
        print("What number is ono")
    elif token == "whitu":
        print("What number is whitu")
    elif token == "waru":
        print("What number is waru")
    elif token == "iwa":
        print("What number is iwa")
    elif token == "tekau":
        print("What number is tekau")
    elif token == "tekau mā tahi":
        print("What number is tekau mā tahi")
    elif token == "tekau mā rua":
        print("What number is tekau mā rua")
    elif token == "tekau mā toru":
        print("What number is tekau mā toru")
    elif token == "tekau mā whā":
        print("What number is tekau mā whā")
    elif token == "tekau mā rima":
        print("What number is tekau mā rima")
    elif token == "tekau mā ono":
        print("What number is tekau mā ono")
    elif token == "tekau mā whitu":
        print("What number is tekau mā whitu")
    elif token == "tekau mā waru":
        print("What number is tekau mā waru")
    elif token == "tekau mā iwa":
        print("What number is tekau mā iwa")
    elif token == "rua tekau":
        print("What number is rua tekau")
    elif token == "rua tekau mā tahi":
        print("What number is rua tekau mā tahi")
    elif token == "rua tekau mā rua":
        print("What number is rua tekau mā rua")
    elif token == "rua tekau mā toru":
        print("What number is rua tekau mā toru")
    elif token == "rua tekau mā whā":
        print("What number is rua tekau mā whā")
    elif token == "rua tekau mā rima":
        print("What number is rua tekau mā rima")
    elif token == "rua tekau mā ono":
        print("What number is rua tekau mā ono")
    elif token == "rua tekau mā whitu":
        print("What number is rua tekau mā whitu? ")
    elif token == "rua tekau mā waru":
        print("What number is rua tekau mā waru? ")
    elif token == "rua tekau mā iwa":
        print("What number is rua tekau mā iwa? ")
    elif token == "toru tekau":
        print("What number is toru tekau? ")

