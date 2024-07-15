while True:
    # Display menu options
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    # User input for operation choice
    choice = input("Enter your choice: ")

    # Check if the user wants to quit
    if choice == "quit":
        break

    # Check if the choice is valid
    if choice not in ["add", "subtract", "multiply", "divide"]:
        print("Invalid input")
        continue

    # Input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the selected operation
    if choice == "add":
        result = num1 + num2
    elif choice == "subtract":
        result = num1 - num2
    elif choice == "multiply":
        result = num1 * num2
    elif choice == "divide":
        if num2 == 0:
            print("Cannot divide by zero")
            continue
        else:
            result = num1 / num2

    print("Result: ", result)
