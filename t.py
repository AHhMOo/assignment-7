def add(a,b):
    return a + b

def subtract(a,b):
    return a - b 

def multiply(a,b):
    return a  * b

def divide(a,b):
    if b == 0:
        return "Error: Division by zero is undefined."
    else:
        return a / b
    

def calculator():
    print("Welcome to the calculator!")
    while True:

        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = int(input("Enter choice (1/2/3/4/5): "))
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == 2:
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == 3:
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == 4:
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        elif choice == 5:
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a valid number (1/2/3/4/5).")

calculator()
#we can do it without calculator() def but i prefer to do it with it to make it more easier to call 



