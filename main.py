import sys
from menu import MENU
from menu import resources
import os
# TODO: 1. Define the variables & functions we need
money = 0


def order_function():
    """Asks what users wants."""
    answer = input("\nWhat would you like? (espresso/latte/cappuccino):\n")
    while answer != "espresso" and answer != "latte" and answer != "cappuccino" and answer != "report" and answer != "off":
        print("Invalid choice !")
        answer = input("\nWhat would you like? (espresso/latte/cappuccino):\n")
    return answer


def print_report():
    """Prints a report of resources available."""
    os.system("cls")
    print("\nPlease see available resources below:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def resources_availability():
    resources_req = MENU[order]["ingredients"]
    if resources["water"] >= resources_req["water"]:
        if resources["milk"] >= resources_req["milk"]:
            if resources["coffee"] >= resources_req["coffee"]:
                return True
            else:
                print("Sorry, there is not enough coffee for your selection.")
                print("Please try something else.")
                return False
        else:
            print("Sorry, there is not enough milk for your selection.")
            print("Please try something else.")
            return False
    else:
        print("Sorry, there is not enough water for your selection.")
        print("Please try something else.")
        return False


def process_coins():
    print(f"The {order} cost is ${MENU[order]["cost"]} -> Please insert coins.")
    quarters = int(input("how many quarters ($0.25) ?"))
    dimes = int(input("how many dimes ($0.10) ?"))
    nickles = int(input("how many nickles ($0.05) ?"))
    pennies = int(input("how many pennies ($0.01) ?"))
    money_insert = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return money_insert


def resources_filling():
    maintenance_operation = int(input("Top up resources - type '1'\nWithdraw funds - type '2'\n"))
    if maintenance_operation == 1:
        water_fill = int(input("How much water do you want to add? (ml)"))
        milk_fill = int(input("How much milk do you want to add? (ml)"))
        coffee_fill = int(input("How much coffee do you want to add? (g)"))
        resources["water"] = resources["water"] + water_fill
        resources["milk"] = resources["milk"] + milk_fill
        resources["coffee"] = resources["coffee"] + coffee_fill
        print("Thank you! Your new resources levels are shown below:")
        print_report()


# TODO: 2. Prompt user by asking "What would you like? (espresso/latte/cappuccino):”
os.system("cls")
order = order_function()

while order != "off":
    # TODO 3. Print report
    if order == "report":
        print_report()
        order = order_function()

    # TODO 5. Check resources sufficient?
    available_resources = resources_availability()
    if not available_resources:
        order = order_function()
    else:
        # TODO 6. Process coins
        money_in = process_coins()

    # TODO 7. Check transaction successful?
        while money_in < MENU[order]["cost"]:
            print(f"\nNot enough money for your {order}")
            print(f"Inserted amount: ${money_in}.")
            print(f"Here is ${money_in} in refund.")
            money_in = process_coins()
        else:
            # TODO 8. Make Coffee
            change = money_in - MENU[order]["cost"]
            money = money + (money_in - change)
            # adjust resources levels:
            resources["water"] = resources["water"] - MENU[order]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU[order]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU[order]["ingredients"]["coffee"]
            print(f"\nHere is ${change} in change.")
            print(f"And here is your {order} ☕. Enjoy !\n")
            order = order_function()

# TODO: 4. Turn off the Coffee Machine by entering “off” to the prompt.
while order == "off":
    print("Maintenance Mode")
    resources_filling()
    order = order_function()

# BUGS
# * when inserting 4 x 0.25, 4 x 0.10, 4 x0.05 and 4 x 0.01 coins for a 1.5 espresso, -
# # - the change comes as $0.1399999999999999

    #sys.exit()
