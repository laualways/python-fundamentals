from game_data import MENU, resources

espresso_cost = MENU['espresso']['cost']
latte_cost = MENU['latte']['cost']
cappuccino_cost = MENU['cappuccino']['cost']
profit = 0

coffe_machine_on = True

def paying():
    pay_quarters = float(input("How many quarters? $"))
    pay_dimes = float(input("How many dimes? $"))
    pay_nickles = float(input("How many nickles? $"))
    pay_pennies = float(input("How many pennies? $"))
    money_insert = (pay_quarters / 4) + (pay_dimes / 10) + (pay_nickles / 20) + (pay_pennies / 100)
    return money_insert

    # print(f"This is your money : ${money_insert}")


while coffe_machine_on:

    drink_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()


    if drink_choice == "espresso":
        # water_resources = resources['water']
        # menu_espresso_water = MENU['espresso']['ingredients']['water']
        if resources['water'] >= MENU['espresso']['ingredients']['water'] and resources['coffee'] >= MENU['espresso']['ingredients']['coffee']:
            print("Please insert coins.")
            payment = paying()
            if payment - espresso_cost >= 0:
                resources['water'] -= MENU['espresso']['ingredients']['water']
                resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
                remainder_payment = round(payment - espresso_cost, 2)
                print(f"This is your remainder: ${remainder_payment}")
                print("Enjoy your espresso!")
                profit += espresso_cost
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            if resources['water'] < MENU['espresso']['ingredients']['water']:
                print("Sorry you do not have enough water.")
            elif resources['coffee'] < MENU['espresso']['ingredients']['coffee']:
                print("Sorry you do not have enough coffee.")
            elif resources['milk'] < MENU['espresso']['ingredients']['milk']:
                print("Sorry you do not have enough milk.")


    if drink_choice == "latte":
        # water_resources = resources['water']
        # menu_espresso_water = MENU['latte']['ingredients']['water']
        if resources['water'] >= MENU['latte']['ingredients']['water'] and resources['coffee'] >= MENU['latte']['ingredients']['coffee'] and resources['milk'] >= MENU['latte']['ingredients']['milk']:
            print("Please insert coins.")
            payment = paying()
            if payment - latte_cost >= 0:
                resources['water'] -= MENU['latte']['ingredients']['water']
                resources['coffee'] -= MENU['latte']['ingredients']['coffee']
                resources['milk'] -= MENU['latte']['ingredients']['milk']
                remainder_payment = round(payment - latte_cost, 2)
                print(f"This is your remainder: ${remainder_payment}")
                print("Enjoy your latte!")
                profit += latte_cost
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            if resources['water'] < MENU['latte']['ingredients']['water']:
                print("Sorry you do not have enough water.")
            elif resources['coffee'] < MENU['latte']['ingredients']['coffee']:
                print("Sorry you do not have enough coffee.")
            elif resources['milk'] < MENU['latte']['ingredients']['milk']:
                print("Sorry you do not have enough milk.")

    if drink_choice == "cappuccino":
        # water_resources = resources['water']
        # menu_espresso_water = MENU['cappuccino']['ingredients']['water']
        if resources['water'] >= MENU['cappuccino']['ingredients']['water'] and resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee'] and resources['milk'] >= MENU['cappuccino']['ingredients']['milk']:
            print("Please insert coins.")
            payment = paying()
            if payment - cappuccino_cost >= 0:
                resources['water'] -= MENU['cappuccino']['ingredients']['water']
                resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
                resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
                remainder_payment = round(payment - cappuccino_cost, 2)
                print(f"This is your remainder: ${remainder_payment}")
                print("Enjoy your cappuccino!")
                profit += cappuccino_cost
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            if resources['water'] < MENU['cappuccino']['ingredients']['water']:
                print("Sorry you do not have enough water.")
            elif resources['coffee'] < MENU['cappuccino']['ingredients']['coffee']:
                print("Sorry you do not have enough coffee.")
            elif resources['milk'] < MENU['cappuccino']['ingredients']['milk']:
                print("Sorry you do not have enough milk.")


    if drink_choice == "off":
        coffe_machine_on = False
        print("You turned off the coffee machine.")
    elif drink_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")