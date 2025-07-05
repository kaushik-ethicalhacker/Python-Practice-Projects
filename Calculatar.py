def calculator(f,o,t):
    s = 0

    def add(n1, n2):
        return n1 + n2
    def subtract(n1, n2):
        return n1 - n2
    def multiply(n1, n2):
        return n1 * n2
    def divide(n1, n2):
        return n1 / n2
    key = {
        "+":add,"-":subtract,"*":multiply,"/":divide,
    }
    if o in key:
        r = key[o](f,t)
        s+=r
        return s
    else:
        print("Invalid operator")
        return None

def start():
    something=True
    logo = r"""
     _____________________
    |  _________________  |
    | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    """
    print(logo)
    first = float(input("Enter your first number:\n"))
    while something:
        second = input(" + \n - \n * \n / \nChoose a mathematical operation:\n")
        third = float(input("Enter your second number:\n"))
        result = calculator(first,second,third)
        if result is None:
            something = False
        else:
            print(f"{first} {second} {third}= {result}")
            again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:\n").lower()
            if again == "y":
                something = True
                first = result
            else:
                something = False
                print("\n"*20)
                start()
start()