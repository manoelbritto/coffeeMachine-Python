from coffee_option import MENU
from coffee_option import resources


def report_machine(money):
    """When the user enters “report” to the prompt, a report should be generated that shows
    the current resource values."""
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffe: {resources['coffee']}g\n"
          f"Money: ${money}")


def check_resources(water, coffee, milk):
    """Check resources sufficient"""
    if resources['water'] <= water:
        print("Sorry the is not enough water")
        return False
    elif resources['milk'] <= milk:
        print("Sorry the is not enough milk")
        return False

    elif resources['coffee'] <= coffee:
        print("Sorry the is not enough coffee")
        return False
    return True


def process_coin():
    """When the user chooses a drink, the program should check if there are enough
    resources to make that drink."""


def check_transaction():
    """Check that the user has inserted enough money to purchase the drink they selected."""


def make_coffee(coffee_type):
    """If the transaction is successful and there are enough resources to make the drink the
    user selected, then the ingredients to make the drink should be deducted from the
    coffee machine resources."""

    if coffee_type == "espresso":
        water = MENU[coffee_type]["ingredients"]["water"]
        coffee = MENU[coffee_type]["ingredients"]["coffee"]
        if check_resources(water, coffee, milk=0):
            resources['water'] -= water
            resources['coffee'] -= coffee

    else:
        water = MENU[coffee_type]["ingredients"]["water"]
        coffee = MENU[coffee_type]["ingredients"]["coffee"]
        milk = MENU[coffee_type]["ingredients"]["milk"]
        if check_resources(water, coffee, milk):
            resources['water'] -= water
            resources['coffee'] -= coffee
            resources['milk'] -= milk


def machine_operation():
    machine_on = True
    money_received = 0.0
    while machine_on:
        option = input("What would you like? (espresso/latte/cappuccino):").lower()
        if option == "report":
            report_machine(money_received)

        else:
            make_coffee(option)

        if option == 'off':
            machine_on = False


machine_operation()
