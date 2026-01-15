print("--- 📖 My Mini Dictionary ---")
print("1. English -> Turkish 🇬🇧 🇹🇷")
print("2. Turkish -> English 🇹🇷 🇬🇧")

choice = input("Select Mode (1 or 2): ").strip()

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

if choice == '2':
    active_dict = tr_to_eng
    prompt_text = "Bir Türkçe kelime yaz: "
    flag = "🇹🇷 -> 🇬🇧"
else:
    active_dict = eng_to_tr
    prompt_text = "Enter an English word: "
    flag = "🇬🇧 -> 🇹🇷"

print(f"\n--- Mode Activated: {flag} ---")
print("Type 'q' to quit.\n")


while True:
    word = input(prompt_text).strip().title()

    if word == 'Q' or word == 'Quit' or word == 'Çıkış':
        print("Bye / Hoşça kal! 👋")
        break

    if word in active_dict:
        print(f"✅ {word} = {active_dict[word]}\n")
    else:
        print(f"❌ '{word}' not found in database.\n{'-'*20}\n❌ '{word}' kütüphanede bulunmadı.")