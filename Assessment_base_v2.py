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


# Function to generate random token
def generate_token(balance):

    rounds_played = 0
    play_again = ""

    # Test loop to generate 5 tokens
    while play_again != "x":
        rounds_played -= 1  # keep track of rounds
        print(formatter(".", f"Question {rounds_played}"))
        print()
        number = random.randint(1, 100)

        # adjust balance
        # if the random number is between 1 and 5
        # user gets a unicorn (add $4 to balance)
        if 1 <= number <= 5:
            balance += 4
            print(formatter("!", "Congratulations, you got a unicorn"))
            print()

        # if the random number is between 6 and 36
        # user gets a donkey (subtract $1 from balance)
        elif 6 <= number <= 36:
            balance -= 1
            print(formatter("D", "Bad luck, you got a donkey"))
            print()

        # in all other cases the token must be a horse or a zebra
        # (subtract $0.50 from the balance in either case)
        else:
            # if the number is even, set the token to zebra
            if number % 2 == 0:
                balance -= .50
                print(formatter("Z", "You got a zebra"))
                print()

            # otherwise, set the token to horse
            else:
                balance -= .50
                print(formatter("H", "You got a horse"))
                print()

        # output
        print(f"Your score is now: {balance}/ {starting_balance}")
        if balance < 1:
            print("\nYou have answered all your questions well done!!!")
            play_again = "x"
        else:
            play_again = input("\nDo you want to play again ?\n<enter> to play"
                               "again or 'X' to exit ").lower()
        print()
    return balance


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


# ask the user how much they want to play with
starting_balance = num_check("How many questions would you like to answer? (between 10 - 30) ", 10, 30)
print(f"You are going to answer {starting_balance}")


closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You started with ${starting_balance}")
print(f"and leave with ${closing_balance}")
print()
print(formatter("*", "Goodbye"))
