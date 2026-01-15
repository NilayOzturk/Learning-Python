import sys
print("--- 📖 My Mini Dictionary ---")

eng_to_tr = {
    "Apple": "Elma",
    "Book": "Kitap",
    "Computer": "Bilgisayar",
    "Mouse": "Fare",
    "School": "Okul"
}

tr_to_eng = {
    "Elma": "Apple",
    "Kitap": "Book",
    "Bilgisayar": "Computer",
    "Fare": "Mouse",
    "Okul": "School"
}

print("Type 'q' to quit.\n")


while True:
    print("\n" + "="*30)
    print("1. English -> Turkish 🇬🇧 🇹🇷")
    print("2. Turkish -> English 🇹🇷 🇬🇧")
    print("(Type 'q' to exit program)")

    choice = input("Select Mode (1 or 2): ").strip().lower()

    if choice == 'q':
        print("Goodbye! 👋")
        break

    if choice == '2':
        active_dict = tr_to_eng
        prompt_text = "Bir Türkçe kelime yaz (Menü için 'm'): "
        flag = "🇹🇷 -> 🇬🇧"
    else:
        active_dict = eng_to_tr
        prompt_text = "Enter an English word (Type 'm' for Menu): "
        flag = "🇬🇧 -> 🇹🇷"

    print(f"\n--- Mode Activated: {flag} ---")

    while True:
        word = input(prompt_text).strip().title()

        if word == 'M':
            print("Returning to menu...")
            break

        if word == 'Q' or word == 'Quit' or word == 'Çıkış' or word == 'Ç':
            print("Bye/Hoşça kal!")
            sys.exit()
    
        if word in active_dict:
            print(f"✅ {word} = {active_dict[word]}\n")
        else:
            print(f"❌ '{word}' not found in database.\n{'-'*20}\n❌ '{word}' kütüphanede bulunmadı.\n")