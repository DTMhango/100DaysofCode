# Initial ingredient quantities and total amount collected
ingredients = {
    'water': 3000,
    'milk': 1000,
    'coffee': 500,
    'money': 0
}

# Drink recipes and prices
menu = {
    'latte': {'water': 225, 'milk': 50, 'coffee': 20, 'price': 2.5},
    'espresso': {'water': 200, 'milk': 75, 'coffee': 30, 'price': 2.0},
    'cappuccino': {'water': 250, 'milk': 25, 'coffee': 35, 'price': 3.0}
}

# Function to print report of ingredients and money
def print_report():
    print(f"Water: {ingredients['water']}ml\nMilk: {ingredients['milk']}ml\nCoffee: {ingredients['coffee']}g\nMoney: ${ingredients['money']}")

# Function to check if there are sufficient ingredients
def check_resources(drink):
    for ingredient in menu[drink]:
        if menu[drink][ingredient] > ingredients[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

# Function to accept payment and return change
def process_coins(drink):
    cost = menu[drink]['price']
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickels + pennies
    if total < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        change = round(total - cost, 2)
        print(f"Here is ${change} in change.")
        ingredients['money'] += cost
        return True

# Function to make the drink
def make_drink(drink):
    for ingredient in menu[drink]:
        ingredients[ingredient] -= menu[drink][ingredient]
    print(f"Here is your {drink}. Enjoy!")

# Main function to run the coffee machine
def run_coffee_machine():
    is_on = True
    while is_on:
        choice = input("What would you like? (latte/espresso/cappuccino): ")
        if choice == 'off':
            is_on = False
        elif choice == 'report':
            print_report()
        else:
            if check_resources(choice):
                if process_coins(choice):
                    make_drink(choice)

run_coffee_machine()
