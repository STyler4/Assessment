"""Component 3 (random tokens) v1
Generates random choice of tokens in random order"""

import random

tokens = ["tahi", "rua", "toru", "whā", "rima", "ono",
          "whitu", "waru", "iwa", "tekau", "tekau mā tahi", "tekau mā rua",
          "tekau mā toru", "tekau mā whā", "tekau mā rima", "tekau mā ono",
          "tekau mā whitu", "tekau mā waru", "tekau mā iwa", "rua tekau",
          "rua tekau mā tahi", "rua tekau mā rua", "rua tekau mā toru",
          "rua tekau mā whā", "rua tekau mā rima", "rua tekau mā ono",
          "rua tekau mā whitu", "rua tekau mā waru", "rua tekau mā iwa", "toru tekau"]

# Testing loop to generate 30 questions
for item in range(1):
    token = random.choice(tokens)
    if token == "tahi":
        print("tahi")
    elif token == "rua":
        print("rua")
    elif token == "toru":
        print("toru")
    elif token == "whā":
        print("whā")
    elif token == "rima":
        print("rima")
    elif token == "ono":
        print("ono")
    elif token == "whitu":
        print("whitu")
    elif token == "waru":
        print("waru")
    elif token == "iwa":
        print("iwa")
    elif token == "tekau":
        print("tekau")
    elif token == "tekau mā tahi":
        print("tekau mā tahi")
    elif token == "tekau mā rua":
        print("tekau mā rua")
    elif token == "tekau mā toru":
        print("tekau mā toru")
    elif token == "tekau mā whā":
        print("tekau mā whā")
    elif token == "tekau mā rima":
        print("tekau mā rima")
    elif token == "tekau mā ono":
        print("tekau mā ono")
    elif token == "tekau mā whitu":
        print("tekau mā whitu")
    elif token == "tekau mā waru":
        print("tekau mā waru")
    elif token == "tekau mā iwa":
        print("tekau mā iwa")
    elif token == "rua tekau":
        print("rua tekau")
    elif token == "rua tekau mā tahi":
        print("rua tekau mā tahi")
    elif token == "rua tekau mā rua":
        print("rua tekau mā rua")
    elif token == "rua tekau mā toru":
        print("rua tekau mā toru")
    elif token == "rua tekau mā whā":
        print("rua tekau mā whā")
    elif token == "rua tekau mā rima":
        print("rua tekau mā rima")
    elif token == "rua tekau mā ono":
        print("rua tekau mā ono")
    elif token == "rua tekau mā whitu":
        print("rua tekau mā whitu")
    elif token == "rua tekau mā waru":
        print("rua tekau mā waru")
    elif token == "rua tekau mā iwa":
        print("rua tekau mā iwa")
    elif token == "toru tekau":
        print("toru tekau")
   
