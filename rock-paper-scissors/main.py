import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# choices list of rock, paper and scissors
choices_list = [rock, paper, scissors]

# user and computer choices
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

# print user and computer choices
print(choices_list[user_choice])
print("Computer Chose: \n" + choices_list[computer_choice])

# compare the choices and print the result
if user_choice == computer_choice:
    print("Draw!")

elif user_choice == 0:
    if computer_choice == 1:
        print("You Lose!")
    else:
        print("You Win!")

elif user_choice == 1:
    if computer_choice == 2:
        print("You Lose!")
    else:
        print("You Win!")

else:
    if computer_choice == 0:
        print("You Lose!")
    else:
        print("You Win!")
