print("--- Super Calculator ---")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("Choose an operation (1/2/3/4): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == "1":
    result = num1 + num2
    print("Result: " + str(result))
elif choice == "2":
    result = num1 - num2
    print("Result: " + str(result))
elif choice == "3":
    result = num1 * num2
    print("Result: " + str(result))
elif choice == "4":
    result = num1 / num2
    print("Result: " + str(result))
else:
    print("Invalid choice!")