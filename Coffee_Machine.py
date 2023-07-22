from clear import clear
# Define ingredients dictionary - money is cumulated as drinks are made, hence 0 an onset
ingredients = {
    'water': 3000,
    'milk': 500,
    'coffee': 500,
    'money': 0
}
# Define the menu dictionary - components needed fro ingredients for each drink
menu = {
    'latte': {'water': 225, 'milk': 50, 'coffee': 20, 'price': 2.5,},
    'espresso': {'water': 200, 'milk': 75, 'coffee': 30, 'price': 2.00,},
    'cappuccino': {'water': 200, 'milk': 75, 'coffee': 30, 'price': 3.00,},
}

# Get report of current status of ingredients and money in coffee machine
def get_report():
    print(f"Water: {ingredients['water']};\nMilk {ingredients['milk']};\nCoffee: {ingredients['coffee']};\nMoney: ${ingredients['money']}")

# Check if resources for the user requested drink are sufficient
def check_resources(drink):
    """Checks the available resources in the coffee"""
    for ingredient in menu[drink]:
        if ingredient != 'price':
            if ingredients[ingredient] < menu[drink][ingredient]:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
    return True

# Process the amount paid by the user and return change if necessary
def process_coins(drink):
    """Processes the user's payment and returns change when necessary if payment is sufficient for selected drink """
    cost = menu[drink]['price']
    print(f"The cost of the drink is ${cost}. Please insert coins: ")
    quarters = int(input("How many Quarters?: ")) * 0.25
    dimes = int(input("How many Dimes?: ")) * 0.1
    nickels = int(input("How many Nickels?: ")) * 0.05
    pennies = int(input("How many Pennies?: ")) * 0.01
    total_paid = quarters + nickels + dimes + pennies
    if total_paid < cost:
        print("Sorry, that's not enough money. Please take back your coins.")
        return False
    else:
        change = round(total_paid - cost, 2)
        print(f"Here is your change: ${change}")
        ingredients['money'] += cost
        return True

# Make the drink and decrease the ingredients accordingly
def make_drink(drink):
    """Makes the drink and decreases the quantity of available ingredients"""
    for ingredient in menu[drink]:
        if ingredient != 'price':
            ingredients[ingredient] -= menu[drink][ingredient]
    print(f"Here is your {drink}. Enjoy!")

def coffee_machine():
    user_request = input("What would you like?\n").lower()
    if user_request == 'off':
        return
    elif user_request == 'report':
        get_report()
        coffee_machine()
    elif user_request in ['latte', 'espresso', 'cappuccino']:
        if check_resources(user_request):
            if process_coins(user_request):
                make_drink(user_request)
                coffee_machine()
    elif user_request not in ['latte', 'espresso', 'cappuccino']:
        print("Sorry, invalid request. Please choose: 'Latte', 'Espresso' or ' Cappuccino'.")
        coffee_machine()

coffee_machine()
