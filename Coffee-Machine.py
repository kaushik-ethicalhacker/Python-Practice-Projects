MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def machine(drink):
    global profit
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    q = int(input("Please insert coin.\n"
                  "How many quarters?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickles?: "))
    p = int(input("How many pennies?: "))
    total = q * quarters + d * dimes + n * nickles + p * pennies

    drink_info = MENU[drink]
    ingredients = drink_info['ingredients']
    cost = drink_info['cost']

    if total < cost:
        return "Sorry that's not enough money. Money refunded."

    for item in ingredients:
        if resources[item] <  ingredients[item]:
            return "Sorry, you don't have enough resources to do that."
    for item in ingredients:
        resources[item] -= ingredients[item]

    change = round(total-cost,2)
    profit += cost
    return (f"Here is ${change} in change.\nHere is your {drink} ☕️. Enjoy!")


def main():
    run = True
    while run:
        print("\n"*1)
        ask = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if ask in MENU:
            print(machine(ask))
        elif ask == "report":
            global profit
            print(f"Water: {resources["water"]}ml \nMilk: {resources["milk"]}ml \nCoffee: {resources["coffee"]}gm")
            print(f"Money: ${profit}")
        elif ask == "off":
            break
        else:
            print("Invalid input.")
            run = False




main()




