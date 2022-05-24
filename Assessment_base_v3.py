"""LU base component
Components added after they have been created and tested"""


# yes/no checking function
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output 'Program Continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output 'Display Instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please answer 'yes or 'no': ")


# function to display instructions
def instructions():
    print()
    print(formatter("*", "How to play"))
    print()
    print("Choose the amount of questions you want to answer - must be between 10 and 30")
    print()
    print("Then press <enter> to play. You will get a random question about numbers"
          " for example, what is the number tahi? "
          "The answer would be '1' ")
    print()


# number checking function
def num_check(question, low, high):
    error = "That was not a valid input\n" \
            "Please enter a number between {} and {}\n".format(low, high)

    # Keep asking until a valid amount (10-30) is entered
    while True:
        try:
            # ask for amount
            response = int(input(question))

            # check for number within the required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# questions
def num_questions(balance):
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


# function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main routine go here...
print(formatter("-", "Welcome to the maori number quiz"))
print()

played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()


# ask the user how many questions they want to answer
starting_balance = num_check("How many questions would you like to answer? (between 10 - 30) ", 10, 30)
print(f"You are going to answer {starting_balance} questions")




