
# Basic Calculator Using Python

## Overview

This script implements a basic calculator in Python, allowing users to perform fundamental arithmetic operations. It is designed for ease of use and serves as a great way to practice coding concepts such as loops, conditionals, and user input handling.

## Features

- **Basic Operations:** Supports addition, subtraction, multiplication, and division.
- **Error Handling:** Prevents division by zero and provides user feedback for invalid inputs.
- **User-Friendly Interface:** Continuous interaction until the user decides to quit the program.

## Table of Contents

1. [Installation](#installation)
2. [How to Use](#how-to-use)
3. [Code Explanation](#code-explanation)
4. [Example Usage](#example-usage)
5. [Future Improvements](#future-improvements)
6. [License](#license)

## Installation

To run this calculator, you need to have Python installed on your computer. You can download Python from the official website: [python.org](https://www.python.org/downloads/).

Once Python is installed, you can simply run the script using the command line:

```bash
python basic_calculator.py
```

## How to Use

1. **Start the Program:**
   - Run the script in your terminal or command prompt.
   
2. **Choose an Operation:**
   - The program will display a menu with options. Enter your choice:
     - `add` for addition
     - `subtract` for subtraction
     - `multiply` for multiplication
     - `divide` for division
     - `quit` to end the program

3. **Input Numbers:**
   - After selecting an operation, the program will prompt you to enter two numbers for the calculation.

4. **View Results:**
   - The program will display the result of the operation. If an invalid operation is attempted (like dividing by zero), an error message will be shown.

## Code Explanation

Here’s a brief breakdown of the code:

```python
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
```

- **Loop:** The `while True` loop keeps the program running until the user decides to quit.
- **Input Handling:** The program checks user input for validity, ensuring only accepted operations are processed.
- **Arithmetic Logic:** Each arithmetic operation is handled using conditionals, with results displayed after computation.

## Example Usage

Here are some example interactions with the calculator:

### Example 1: Addition

```
Options:
Enter 'add' for addition
Enter 'subtract' for subtraction
Enter 'multiply' for multiplication
Enter 'divide' for division
Enter 'quit' to end the program
Enter your choice: add
Enter first number: 5
Enter second number: 3
Result:  8.0
```

### Example 2: Division by Zero

```
Options:
Enter 'add' for addition
Enter 'subtract' for subtraction
Enter 'multiply' for multiplication
Enter 'divide' for division
Enter 'quit' to end the program
Enter your choice: divide
Enter first number: 10
Enter second number: 0
Cannot divide by zero
```

### Example 3: Invalid Input

```
Options:
Enter 'add' for addition
Enter 'subtract' for subtraction
Enter 'multiply' for multiplication
Enter 'divide' for division
Enter 'quit' to end the program
Enter your choice: modulus
Invalid input
```

### Example 4: Quitting the Program

```
Options:
Enter 'add' for addition
Enter 'subtract' for subtraction
Enter 'multiply' for multiplication
Enter 'divide' for division
Enter 'quit' to end the program
Enter your choice: quit
```

## Future Improvements

- **Enhanced User Interface:** Consider implementing a graphical user interface (GUI) using libraries like Tkinter or PyQt.
- **Extended Functionality:** Add more advanced operations like exponentiation, square roots, or trigonometric functions.
- **Persistent Memory:** Implement a feature that allows the calculator to remember previous results and use them in new calculations.

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed!

---

Feel free to add any specific details or additional sections that you think would be helpful!
