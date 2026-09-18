from game_data import MENU, resources

profit = 0
coffe_machine_on = True

def paying():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry you do not have enough {item}.")
            return False
    return True

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Enjoy your {drink_name}!")

while coffe_machine_on:

    drink_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drink_choice == "off":
        coffe_machine_on = False
        print("You turned off the coffee machine.")

    elif drink_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")

    elif drink_choice in MENU:
        drink = MENU[drink_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = paying()
            if payment - drink["cost"] >= 0:
                remainder_payment = round(payment - drink["cost"], 2)
                print(f"This is your remainder: ${remainder_payment}")
                profit += drink["cost"]
                make_coffee(drink_choice, drink["ingredients"])
            else:
                print("Sorry that's not enough money. Money refunded.")