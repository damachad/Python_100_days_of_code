from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

switch_on = True

while switch_on:
    option = input(f"What would you like? ({menu.get_items()}): ").lower()
    if option == "report":
        coffee_maker.report()
        money_machine.report()
    elif option == "off":
        switch_on = False
    else:
        drink = menu.find_drink(option)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
