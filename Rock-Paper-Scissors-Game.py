rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
x = int(input("Welcome to Rock,Paper,Scissors game.\n"
      "What would you like to choose type 0 for rock,1 for paper,2 for scissors?\n").lower())
b = [rock,paper,scissors]
c = [rock,paper,scissors]

if x == 0 or x == 1 or x == 2:
    user = b[x]
    computer = random.choice(c)
    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")
    if user == rock and computer == rock:
        print("IT'S A DRAW")
    elif user == rock and computer == paper:
        print("YOU LOSE")
    elif user == rock and computer == scissors:
        print("YOU WIN")
    elif user == paper and computer == rock:
        print("YOU WIN")
    elif user == paper and computer == paper:
        print("IT'S A DRAW")
    elif user == paper and computer == scissors:
        print("YOU LOSE")
    elif user == scissors and computer == rock:
        print("YOU LOSE")
    elif user == scissors and computer == paper:
        print("YOU WIN")
    elif user == scissors and computer == scissors:
        print("IT'S A DRAW")

else:
    print("You typed invaled number.\nYou lose")

