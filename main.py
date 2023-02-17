import coffee_option
from coffee_option import MENU
from coffee_option import resources


def report_machine(money):
    """When the user enters “report” to the prompt, a report should be generated that shows
    the current resource values."""
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffe: {resources['coffee']}g\n"
          f"Money: ${resources['money']}")


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


def process_coin(coffee_type):
    """When the user chooses a drink, the program should check if there are enough
    resources to make that drink."""
    total_value = MENU[coffee_type]["cost"]
    print(f"coffee_type cost {total_value}")
    quarters = int(input("How many quarters ($0.25)?"))
    dimes = int(input("How many dimes ($0.10)?"))
    nickles = int(input("How many nickles ($0.05)?"))
    pennies = int(input("How many pennies ($0.01)?"))
    client_money = (quarters * 0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)
    return check_transaction (coffee_type, client_money)

def check_transaction(coffee_type, money):
    """Check that the user has inserted enough money to purchase the drink they selected."""
    total_value = MENU[coffee_type]["cost"]
    change = money - total_value
    if change >= 0:
        print(f"This is your change {round(change,2)}")
        resources['money'] += total_value
        return True
    else:
        print(f"Not enough money for {coffee_type}, total value {total_value}, but you enter {round(abs(change),2)}")
        return False


def make_coffee(coffee_type):
    """If the transaction is successful and there are enough resources to make the drink the
    user selected, then the ingredients to make the drink should be deducted from the
    coffee machine resources."""

    if coffee_type == "espresso":
        water = MENU[coffee_type]["ingredients"]["water"]
        coffee = MENU[coffee_type]["ingredients"]["coffee"]
        if check_resources(water, coffee, milk=0):
            if process_coin(coffee_type):
                resources['water'] -= water
                resources['coffee'] -= coffee

    else:
        water = MENU[coffee_type]["ingredients"]["water"]
        coffee = MENU[coffee_type]["ingredients"]["coffee"]
        milk = MENU[coffee_type]["ingredients"]["milk"]
        if check_resources(water, coffee, milk):
            if process_coin(coffee_type):
                resources['water'] -= water
                resources['coffee'] -= coffee
                resources['milk'] -= milk


def machine_operation():
    options = ['espresso', 'latte', 'cappuccino', 'report', 'off']
    right_value = True
    machine_on = True
    money_received = 0.0
    while machine_on:
        while right_value:
            option = input("☕ What would you like? (espresso/latte/cappuccino):").lower()
            if option in options:
                right_value = False
            else:
                print ("Sorry, your have to Type (espresso/latte/cappuccino): ")
        if option == "report":
            report_machine(money_received)
        elif option == 'off':
                machine_on = False
        else:
            make_coffee(option)


        right_value = True

print (coffee_option.logo)
machine_operation()
