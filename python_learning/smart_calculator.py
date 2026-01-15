while True:
    print("\n--- Super Calculator ---")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("q. Quit (Exit)")

    choice = input("Choose an operation: ")

    if choice == "q" or choice == "Q":
        print("Goodbye!")
        break

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == "1":
        print(f"Result: {num1 + num2}")
    elif choice == "2":
        print(f"Result: {num1 - num2}")
    elif choice == "3":
        print(f"Result: {num1 * num2}")
    elif choice == "4":
        print(f"Result: {num1 / num2}")
    else:
        print("Invalid choice!")