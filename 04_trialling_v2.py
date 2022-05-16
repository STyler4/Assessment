"""Get questions for user
trial 2"""

import random


def computer():
    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        return "tahi"
    elif computer_choice == 2:
        return "rau"
    else:
        return "toru"


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
