from game_data import MENU, resources

espresso_cost = MENU['espresso']['cost']
latte_cost = MENU['latte']['cost']
cappuccino_cost = MENU['cappuccino']['cost']

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
                remainder_payment = payment - espresso_cost
                print(f"This is your remainder: ${remainder_payment}")
                print("Enjoy your espresso!")
            else:
                print("Sorry that's not enough money. Money refunded.")

        else:
            print("Sorry you do not have enough resources.")

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
                remainder_payment = payment - latte_cost
                print(f"This is your remainder: ${remainder_payment}")
                print("Enjoy your latte!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry you do not have enough resources.")

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
                remainder_payment = payment - cappuccino_cost
                print(f"This is your remainder: ${remainder_payment}")
                print("Enjoy your cappuccino!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry you do not have enough resources.")


    if drink_choice == "off":
        coffe_machine_on = False
        print("You turned off the coffee machine.")


    if drink_choice == "report":
        reso = ""
        for items in resources:
            reso += f"{items.title()} : {resources[items]} \n "
        print(f"You still have: \n {reso}")




