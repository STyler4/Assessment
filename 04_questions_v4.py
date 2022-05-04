"""Component 2 (question) v4
Changing v3 into a function
Also needed to change user_balance to the more generic variable name 'response'
and to change the condition and position of the number comparison into the loop
to make the function recyclable"""


def num_check(questions, low, high):
    error = "That was not a valid input\n" \
            "Please enter a number between {} and {}\n".format(low, high)

    # Keep asking until a valid amount (1-10) is entered
    while True:
        try:
            # ask for amount
            response = int(input(questions))

            # check for number within the required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine
question = num_check("How many questions do you want to answer? ", 10, 30)
print(f"You are going to answer {question} questions")
