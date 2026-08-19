from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = MoneyMachine()
maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    choice = input(f"What would you like? ({menu.get_items()})")
    if choice == "report":
        maker.report()
        money.report()
    elif choice in menu.get_items():
        drink = menu.find_drink(choice)
        if maker.is_resource_sufficient(drink):
            user_money = money.process_coins()
            if money.make_payment(user_money):
                maker.make_coffee(drink)

