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

money = 0
turn_off = False


def print_menu():
    """list all the drinks in the menu"""
    print("----MENU----")
    for drink in MENU:
        print(f"{drink}: ${MENU[drink]['cost']}")
    print("------------")


# TODO 3: generate report of resources and money
def generate_report():
    """return current remaining resources and money"""
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${money}')


# TODO 4: check resources sufficient
def check_resource(customer_order):
    """check if resource sufficient for the order and apologize if not, return True/False"""
    for ingredient in MENU[order]["ingredients"]:
        if resources[ingredient] < MENU[order]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        else:
            return True


# TODO 6: check transaction, process coins
def transaction(customer_order, quarters, dimes, nickles, pennies):
    """get the ordered drink and inserted coins, reply with the change or refund,
    return the income money."""
    price_in_dollar = MENU[customer_order]["cost"]
    # 1 quarter = 25 cents = 0.25 dollar
    # 1 dime = 10 cents = 0.1 dollar
    # 1 nickle = 5 cents = 0.05 dollar
    # 1 penny = 1 cent = 0.01 dollar
    coins_in_dollar = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    change = round((coins_in_dollar - price_in_dollar), 2)
    if change >= 0:
        print(f"Here is ${change} dollars in change.")
        return price_in_dollar
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0


# TODO 7: make coffee
def make_coffee(customer_order):
    # order = "latte"
    # "latte": {
    # "ingredients": {
    #     "water": 200,
    #     "milk": 150,
    #     "coffee": 24,
    # },
    # resources = {
    #     "water": 300,
    #     "milk": 200,
    #     "coffee": 100,
    # }
    for ingredient in MENU[customer_order]["ingredients"]:
        deducted_amount = MENU[customer_order]["ingredients"][ingredient]
        if ingredient in resources:
            resources[ingredient] -= deducted_amount
    print(f"Here is your {customer_order}. Enjoy!")
    return resources


print_menu()

while not turn_off:
    # TODO 1: print the menu, and prompt user by asking the order
    order = input(" What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: turn off the coffee machine by entering "off" to the prompt
    if order == "off":
        turn_off = True
    # TODO: print report
    elif order == "report":
        generate_report()
    elif check_resource(order):
        print("Please insert coins.")
        quarter = int(input("How many quarters?: "))
        dime = int(input("How many dimes?: "))
        nickle = int(input("How many nickles?: "))
        penny = int(input("How many pennies?: "))
        money += transaction(order, quarter, dime, nickle, penny)
        make_coffee(order)
