"""Component 2 (Questions) v2
Use try/accept and pull error messages out of the loop """

error = "Please enter a whole number between 10 and 30\n"
valid = False

# Keep asking until a valid amount (10-30) is entered
while not valid:
    try:
        # ask for amount
        amount_of_questions = int(input("How many questions do you want to answer? "))

        # check if the amount is too high/low
        if 10 <= amount_of_questions <= 30:
            print(f"You are going to answer {amount_of_questions} questions")
            valid = True
        else:
            print(error)
    except ValueError:
        print(error)


