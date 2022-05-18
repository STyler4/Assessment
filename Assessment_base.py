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
    print("**** How to Play ****")
    print()
    print("The rules of the game will go here")
    print()


# number checking function
def num_check(question, low, high):
    error = "That was not a valid input\n" \
            "Please enter a number between {} and {}\n".format(low, high)

    # Keep asking until a valid amount (1-10) is entered
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


def questions_check():
    import random

    tokens = ["tahi", "rua", "toru", "whā", "rima", "ono",
              "whitu", "waru", "iwa", "tekau", "tekau mā tahi", "tekau mā rua",
              "tekau mā toru", "tekau mā whā", "tekau mā rima", "tekau mā ono",
              "tekau mā whitu", "tekau mā waru", "tekau mā iwa", "rua tekau",
              "rua tekau mā tahi", "rua tekau mā rua", "rua tekau mā toru",
              "rua tekau mā whā", "rua tekau mā rima", "rua tekau mā ono",
              "rua tekau mā whitu", "rua tekau mā waru", "rua tekau mā iwa", "toru tekau"]

    questions = NUMBER_OF_QUESTIONS
    starting_score = 0
    score = starting_score
    token = random.choice(tokens)


# Main routine go here...
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()


# ask the user how much they want to play with
NUMBER_OF_QUESTIONS = num_check("How many questions would you like to answer? ", 10, 30)
print(f"You are going to answer {NUMBER_OF_QUESTIONS} questions")
