def add(n1, n2):
    """Returns the sum of two numbers."""
    return n1 + n2

def subtract(n1, n2):
    """Returns the difference."""
    return n1 - n2

def multiply(n1, n2):
    """Returns the product."""
    return n1 * n2

def divide(n1, n2):
    """Returns the division result. Handles division by zero."""
    if n2 == 0:
        return "Error: Cannot divide by zero!"
    return n1 / n2

print("--- 🧮 Smart Calculator ---")

while True:
    print("\nSelect Operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("Q. Quit")
    
    choice = input("Enter choice (1-4 or Q): ").strip().lower()

    if choice == 'q':
        print("Exiting calculator... Goodbye! 👋")
        break

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("⚠️ Please enter valid numbers only!")
            continue 

        if choice == '1':
            result = add(num1, num2)
            print(f"✅ Result: {result}")

        elif choice == '2':
            result = subtract(num1, num2)
            print(f"✅ Result: {result}")

        elif choice == '3':
            result = multiply(num1, num2)
            print(f"✅ Result: {result}")

        elif choice == '4':
            result = divide(num1, num2)
            print(f"✅ Result: {result}")
    
    else:
        print("❌ Invalid input. Please try again.")