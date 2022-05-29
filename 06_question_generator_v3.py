# questions
def quiz(num_questions):
    score_ = 0
    num_questions_ = num_questions
    rounds = 0

    numbers = ["tahi", "rua", "toru", "whā", "rima", "ono",
               "whitu", "waru", "iwa", "tekau", "tekau mā tahi",
               "tekau mā rua", "tekau mā toru", "tekau mā whā",
               "tekau mā rima", "tekau mā ono", "tekau mā whitu",
               "tekau mā waru", "tekau mā iwa", "rua tekau",
               "rua tekau mā tahi", "rua tekau mā rua", "rua tekau mā toru",
               "rua tekau mā whā", "rua tekau mā rima", "rua tekau mā ono",
               "rua tekau mā whitu", "rua tekau mā waru", "rua tekau mā iwa",
               "toru tekau"]

    answers = ["1", "2", "3", "4", "5", "6",
               "7", "8", "9", "10", "11", "12",
               "13", "14", "15", "16",
               "17", "18", "19", "20",
               "21", "22", "23",
               "24", "25", "26",
               "27", "28", "29", "30"]

    while rounds <= num_questions_:
        rounds += 1
        question = random.choice(numbers)
        attempt = input(f"What number is {question}: ")
        print()

        answer_index = numbers.index(question)
        answer = answers[answer_index]

        if attempt == answer:
            print()
            print(formatter("!", "Well done, that was correct"))
            numbers.pop(answer_index)
            answers.pop(answer_index)
            score_ += 1
            print()
        elif attempt == "":
            print()
            print(formatter("-", "Invalid please try again"))
            print()
        else:
            print()
            print(formatter("^", "Unlucky, that was incorrect"))
            numbers.pop(answer_index)
            answers.pop(answer_index)
            print()
    return score_
