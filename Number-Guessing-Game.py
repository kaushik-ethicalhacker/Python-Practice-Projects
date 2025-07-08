import random
def choose_easy(difficulty):
    a = random.randint(1, 100)
    print(a)
    if difficulty == "easy":
        for x in range(10,0,-1):
            print(f"You have {x} attempts remaining to guess the number.")
            g =  int(input("Make a guess: "))

            if a > g :
                print("Too Low.")
                if x >= 2:
                    print("Guess Again.")
            elif a < g :
                print("Too High")
                if x >= 2:
                    print("Guess Again.")
            elif a == g:
                return f"You got it! The answer was {a}."
        return f"You lost! The answer was {a}."
    else:
        for y in range(5,0,-1):
            print(f"You have {y} attempts remaining to guess the number.")
            g = int(input("Make a guess: "))
            if a > g :
                print("Too Low")
                if y >= 2:
                    print("Guess Again.")
            elif a < g :
                print("Too High")
                if y >= 2:
                    print ("Guess Again.")
            elif a == g:
                return f"You got it! The answer was {a}."
        return f"You lost! The answer was {a}."

def guess():
    logo = r'''
      / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
     / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
    / /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
    \____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|
    '''
    again = True
    while again:
        print(logo)
        ca = input("welcome to guess the number !\n"
              "I am thinking of a number between 1 and 100.\n"
              "Choose the difficulty. Type 'easy' or 'hard' : ").lower()
        print(choose_easy(ca))
        c = input("Would you like to play again? (y/n): ").lower()
        if c == "n":
            again = False
        else:
            print("\n"*50)
            guess()
guess()
