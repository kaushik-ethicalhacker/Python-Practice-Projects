logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bitting={}
def bit(name,price):
    bitting[name] = price

should_continue = True
while should_continue:
    x = input("What's Your Name?\n")
    y = int(input("What's Your Bit?\n$"))
    bit(x, y)
    w = input("Are there any other bidders? Type 'yes or 'no'.?\n").lower()
    g = max(bitting,key=bitting.get)


    if w == "no":
        should_continue = False
        print(f"The winner is {g} bid is ${bitting[g]}")
    elif w == "yes":
        print("\n"*100)


