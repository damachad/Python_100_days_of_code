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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(item_resources, available_resources):
    """Compares two resources dictionaries and checks if the 
    first has greater values than the second"""
    for item in item_resources:
        if item_resources[item] > available_resources[item]:
            return item


def update_resources(item_resources, available_resources):
    """Updates items in the second dictionary by subtracting
    the value of the item from the first (if present)"""
    for item in available_resources:
        if item in item_resources:
            available_resources[item] -= item_resources[item]


switch_on = True
money = 0

while switch_on:
    option = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if option == "report":
        print(f"Water: {resources['water']}mL")
        print(f"Milk: {resources['milk']}mL")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif option == "off":
        switch_on = False
    else:
        drink = MENU[option]
        if check_resources(drink["ingredients"], resources):
            print(f"Sorry there is not enough {check_resources(drink['ingredients'], resources)}")
        else:
            print("Please insert coins.")
            quarters = 0.25 * float(input("how many quarters?: "))
            dimes = 0.10 * float(input("how many dimes?: "))
            nickles = 0.05 * float(input("how many nickles?: "))
            pennies = 0.01 * float(input("how many pennies?: "))
            total = round((quarters + dimes + nickles + pennies), 2)
            if total < drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = round(total - drink["cost"], 2)
                money += drink["cost"]
                if change > 0:
                    print(f"Here is ${change} in change.")
                update_resources(drink["ingredients"], resources)
                print(f"Here is your {option} ☕️. Enjoy!")
