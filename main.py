def add(num1, num2): return num1 + num2
def sub(num1, num2): return num1 - num2
def mul(num1, num2): return num1 * num2
def div(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Error: Zero cannot divide any number"

operations = {
    '1': add,
    '2': sub,
    '3': mul,
    '4': div
}

print("Available operations:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        choice = input("\nEnter the operation (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice. Please select a valid operation.")
            continue

        print(f"The result is: {operations[choice](num1, num2)}")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
