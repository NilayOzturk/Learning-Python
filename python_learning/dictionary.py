print("--- 📖 My Mini Dictionary ---")
print("Type a word to learn its meaning (or 'q' to quit).\n")

dictionary = {
    "Apple": "Elma",
    "Book": "Kitap",
    "Computer": "Bilgisayar",
    "Developer": "Yazılımcı",
    "Bug": "Yazılım hatası (Böcek)"
}

while True:

    word = input("👉 Enter an English word: ").strip().title()

    if word == 'Q' or word == 'Quit':
        print("Goodbye! 👋")
        break

    if word in dictionary:
        meaning = dictionary[word]
        print(f"\n🔎 {word} found!")
        print(f"🇹🇷 Turkish: {meaning}\n")
    else:
        print(f"❌ '{word}' not found in database.\n")