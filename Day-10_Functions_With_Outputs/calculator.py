def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2


def calculate_given_values():
    while True:
        input_dict = {}
        first_number = float(input("Enter your first number"))
        continue_with_first = True
        input_dict["num1"] = first_number
        while continue_with_first:
            operation = input("Enter operation")
            input_dict["operation"] = operation
            second_number = float(input("Enter your second number"))
            input_dict["num2"] = second_number
            result = calculate(num1=input_dict["num1"],
                               num2=input_dict["num2"],
                               operation=input_dict["operation"])
            print(
                f'{input_dict["num1"]} {input_dict["operation"]} {input_dict["num2"]} = {result}'
            )
            should_continue = input(
                f'Do you want to continue with {result}? (y/n)\n').lower()
            if should_continue == "y":
                input_dict["num1"] = result
            elif should_continue == "n":
                continue_with_first = False


calculate_given_values()
