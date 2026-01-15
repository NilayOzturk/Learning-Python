print("---🛒 Virtual Shopping List ---")
print("Type 'q' or 'done' to exit.\n")

shopping_list = []

while True:
    item = input("What would you like to add? :")

    if item.strip().lower() == 'q' or item.strip().lower() == 'done':
        print("Shopping completed! 🏁")
        break

    shopping_list.append(item)
    print(f"{item} added to cart!")

print("Things you need to buy:")

for item in shopping_list:
    print(f"-{item}")

print("\n Have a nice shopping!🌸")