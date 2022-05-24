import random

numbers = ["tahi", "rua", "toru", "whā", "rima", "ono",
           "whitu", "waru", "iwa", "tekau", "tekau mā tahi", "tekau mā rua",
           "tekau mā toru", "tekau mā whā", "tekau mā rima", "tekau mā ono",
           "tekau mā whitu", "tekau mā waru", "tekau mā iwa", "rua tekau",
           "rua tekau mā tahi", "rua tekau mā rua", "rua tekau mā toru",
           "rua tekau mā whā", "rua tekau mā rima", "rua tekau mā ono",
           "rua tekau mā whitu", "rua tekau mā waru", "rua tekau mā iwa", "toru tekau"]

questions = ["1", "2", "3", "4", "5", "6",
             "7", "8", "9", "10", "11", "12",
             "13", "14", "15", "16",
             "17", "18", "19", "20",
             "21", "22", "23",
             "24", "25", "26",
             "27", "28", "29", "30"]


while True:
    question = random.choice(numbers)
    attempt = input(f"What number is {question}: ")

    answer_index = numbers.index(question)
    answer = questions[answer_index]
    score = 0
    number_of_questions = balance
    if attempt == answer:
        print("Well done, that was correct")
        numbers.pop(answer_index)
        questions.pop(answer_index)
        score += 1
        number_of_questions -= 1
    elif attempt == "":
        print("Invalid please try again")
    else:
        print("Unlucky, that was incorrect")
        numbers.pop(answer_index)
        questions.pop(answer_index)
        number_of_questions -= 1
        print(number_of_questions)
