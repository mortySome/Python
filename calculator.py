logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

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

def calculation_func():
    should_con = True
    #first while loop so that the value of first_num is not changed in second one
    while should_con:
        #second while loop so that when the user wants to reset it actually does. 
        print(logo)
        first_num = float(input("What's the first number?: "))
        continue_calculating = True
        while continue_calculating:
            for keys in operations:
                print(keys)
            user_operation = input("Pick an operation: ")
            next_num = float(input("What's the next number?: "))

            calc_process_result = operations[user_operation](first_num, next_num)

            print(f"{first_num} {user_operation} {next_num} = {calc_process_result}")

            continue_or_not = input(f"Type 'y' to continue calculating with {calc_process_result}, or type 'n' to start a new calculation or 'e' to exit: ").lower()
            if continue_or_not == 'y':
                first_num = calc_process_result
            elif continue_or_not == 'n':
                continue_calculating = False
            else:
                continue_calculating = False
                should_con = False
    
    
calculation_func()
