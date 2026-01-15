print("---🛒 Virtual Shopping List ---")
print("Type 'q' or 'done' to exit.\n")

shopping_list = []

while True:
    item = input("What would you like to add? :")

    if item.strip().lower() == 'q' or item.strip().lower() == 'done':
        print("Shopping completed! 🏁")
        break

    item = item.strip().title()

    if item in shopping_list:
        print(f"{item} is already in the list!")
    else:
        shopping_list.append(item) 
        print(f"{item} added to cart!")
    

print("\n 🧾Your Shopping List🧾:")

count = len(shopping_list)

if count <=5:
    print(f"You have {count} items:")
    for item in shopping_list:
        print(f"-{item}")

else:
    print(f"You have {count} items:")
    print(", ".join(shopping_list))

print("\n Have a nice shopping!🌸")