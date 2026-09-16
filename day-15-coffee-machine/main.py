from game_data import MENU, resources

coffe_machine_on = True

while coffe_machine_on:
    drink_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()


    if drink_choice == "espresso":
        # water_resources = resources['water']
        # menu_espresso_water = MENU['espresso']['ingredients']['water']
        if resources['water'] > MENU['espresso']['ingredients']['water'] and resources['coffee'] > MENU['espresso']['ingredients']['coffee']:
            resources['water'] -= MENU['espresso']['ingredients']['water']
            resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
            print(resources)

    if drink_choice == "latte":
        # water_resources = resources['water']
        # menu_espresso_water = MENU['latte']['ingredients']['water']
        if resources['water'] > MENU['latte']['ingredients']['water'] and resources['coffee'] > MENU['latte']['ingredients']['coffee'] and resources['milk'] > MENU['latte']['ingredients']['milk']:
            resources['water'] -= MENU['latte']['ingredients']['water']
            resources['coffee'] -= MENU['latte']['ingredients']['coffee']
            resources['milk'] -= MENU['latte']['ingredients']['milk']
            print(resources)

    if drink_choice == "cappuccino":
        # water_resources = resources['water']
        # menu_espresso_water = MENU['cappuccino']['ingredients']['water']
        if resources['water'] > MENU['cappuccino']['ingredients']['water'] and resources['coffee'] > MENU['cappuccino']['ingredients']['coffee'] and resources['milk'] > MENU['cappuccino']['ingredients']['milk']:
            resources['water'] -= MENU['cappuccino']['ingredients']['water']
            resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
            resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
            print(resources)


    if drink_choice == "off":
        coffe_machine_on = False
