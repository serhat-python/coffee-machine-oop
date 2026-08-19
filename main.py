from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = MoneyMachine()
maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    choice = input(f"What would you like? ({menu.get_items()})").lower()
    if choice == "report":
        maker.report()
        money.report()
    elif choice == "off":
        is_on = False
    elif choice in menu.get_items():
        drink = menu.find_drink(choice)
        if maker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                maker.make_coffee(drink)

