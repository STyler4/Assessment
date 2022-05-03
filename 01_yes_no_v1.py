# Ask the user if they have played before
show_instructions = input("have you played this game before?: ")

# If they say yes, output 'Program Continues'
if show_instructions.lower() == "yes":
    print("program continues")

# If they say no, output 'Display Instructions'
elif show_instructions.lower() == "no":
    print("Display instructions")

# Otherwise - show error
else:
    print("Please answer 'yes or 'no'")
