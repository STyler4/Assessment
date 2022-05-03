"""Component 2 (Questions) v1
Ask user how many questions they would like from 10 to 30.
Check the input is a valid integer between 10 and 30. If
it is that is the amount of questions the user will get """

amount_of_questions = int(input("How many questions do you want to answer"
                                "between 10 and 30? "))

# Keep asking until a valid amount (10-30) is entered
while not 10 <= amount_of_questions <= 30:
    print("Try again, Please enter a whole number between 10 and 30")
    # ask for the input
    amount_of_questions = int(input("How many questions do you want to answer? "))

print(f"You are going to answer {amount_of_questions} questions")
