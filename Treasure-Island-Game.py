print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

a = input("You are on a road now.\nIn which direction you want to go Left or Right?\n").lower()
b = ("You have come to a lake.\n"
     "Do you want to Swim to treasure island or Wait for a boat")
c = ("You have arrived at the island unharmed.There is a house with 3 doors Blue,Yellow and RED.\n"
     "Which door are you gonna choose?")

if a == "Left" or a == "left":
    d = input(b + "\n").lower()
    if d == "Wait" or d == "wait":
        x = input(c + "\n").lower()
        if x == "Yellow" or x == "yellow":
             print("Congratulations! You found the treasure\nYou are a billionaire. You won.")
        elif x == "RED" or x == "red":
              print("You have been eaten by the crabs\nGAME OVER")
        elif x == "Blue" or x == "blue":
             print("You fell in acid\nGAME OVER")
        else:
              print("GAME OVER")
    else:
        print("You don't know swimming.\nGAME OVER")
else:
    print("You went into wrong direction.\nGAME OVER")



