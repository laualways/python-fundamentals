import art

print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

game_over = True

while game_over:
    first_choice = float(input("What's the first number?:   "))
    should_continue = True

    while should_continue:
        for symbol in operations:
            print(symbol)
        pick_operator = input("Pick an operation:    ")
        second_choice = float(input("What's the next number?   "))

        operation_result = operations[pick_operator](
            first_choice, second_choice
        )

        print(
            f"{first_choice} {pick_operator} {second_choice} = {operation_result}"
        )

        continue_operation = input(
            f"Type 'y' to continue calculating with {operation_result}, or type 'n' to start a new calculation:   "
        ).lower()

        if continue_operation == "y":
            first_choice = operation_result
        elif continue_operation == "n":
            should_continue = False
            print("\n" * 20)
            print(art.logo)