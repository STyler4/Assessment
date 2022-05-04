"""Component 2 (question) v3
More efficient method - includes valid range as the basis of the while loop
which eliminates the need to use the 'valid' variable"""

# Main routine
error = "That was not a valid input\n"
question = 0

# Keep asking until a valid amount (1-10) is entered
while not 10 <= question <= 30:
    try:
        # ask for amount
        question = int(input("Please enter a whole number between 10 and 30"
                             "\nHow many questions do you want to answer? "))
        print()

    except ValueError:
        print(error)
print(f"You are going to answer {question} questions")
