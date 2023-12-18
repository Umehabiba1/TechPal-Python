import math


class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error! Division by zero."
        return x / y

    def square(self, x):
        return x ** 2

    # def square_root(self, x):
    #     if x < 0:
    #         return "Error! Cannot calculate square root of a negative number."
    #     return math.sqrt(x)

calculator = Calculator()

while True:
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Square Root")
    print("0. Exit")

    choice = input("Enter choice (0-6): ")

    if choice == '0':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))
        if choice in ('1', '2', '3', '4'):
            num2 = float(input("Enter second number: "))

        if choice == '1':
            result = calculator.add(num1, num2)
        elif choice == '2':
            result = calculator.subtract(num1, num2)
        elif choice == '3':
            result = calculator.multiply(num1, num2)
        elif choice == '4':
            result = calculator.divide(num1, num2)
            
        elif choice == '5':
            result = calculator.square(num1)
        # elif choice == '6':
        #     result = calculator.square_root(num1)

        print(f"Result: {result}")
    else:
        print("Invalid input. Please enter a number between 0 and 6.")
