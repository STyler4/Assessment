"""Get questions for user
trial 1"""

import random


def computer():
    choices = ["tahi", "rau", "toru"]
    computer_choice = random.choice(choices)
    return computer_choice


# Main routine
tahi = 0
rau = 0
toru = 0

for turn in range(1000):
    choice = computer()
    print(f"{choice}")
    if choice == "tahi":
        tahi += 1
    elif choice == "rau":
        rau += 1
    else:
        toru += 1

print()
print(f"After program runs:\n"
      f"\t tahi came up {tahi} times\n"
      f"\t rau came up {rau} times\n"
      f"\t and toru came up {toru} times")
