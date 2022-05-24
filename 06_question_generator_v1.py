import random

numbers = ["tahi", "rua", "toru", "whā", "rima", "ono",
           "whitu", "waru", "iwa", "tekau", "tekau mā tahi", "tekau mā rua",
           "tekau mā toru", "tekau mā whā", "tekau mā rima", "tekau mā ono",
           "tekau mā whitu", "tekau mā waru", "tekau mā iwa", "rua tekau",
           "rua tekau mā tahi", "rua tekau mā rua", "rua tekau mā toru",
           "rua tekau mā whā", "rua tekau mā rima", "rua tekau mā ono",
           "rua tekau mā whitu", "rua tekau mā waru", "rua tekau mā iwa", "toru tekau"]

questions = ["tahi", "rua", "toru", "whā", "rima", "ono",
             "whitu", "waru", "iwa", "tekau", "tekau mā tahi", "tekau mā rua",
             "tekau mā toru", "tekau mā whā", "tekau mā rima", "tekau mā ono",
             "tekau mā whitu", "tekau mā waru", "tekau mā iwa", "rua tekau",
             "rua tekau mā tahi", "rua tekau mā rua", "rua tekau mā toru",
             "rua tekau mā whā", "rua tekau mā rima", "rua tekau mā ono",
             "rua tekau mā whitu", "rua tekau mā waru", "rua tekau mā iwa", "toru tekau"]

question = random.choice(numbers)
attempt = input(f"What number is {question}: ")

answer_index = numbers.index(question)
answer = questions[answer_index]

if attempt == answer:
    print("Well done, that was correct")
    numbers.pop(answer)

else:
    print("Unlucky, that was incorrect")
    numbers.pop(answer)
