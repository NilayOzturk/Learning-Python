import json

# 1. Elimizde bir veri var
my_dictionary = {
    "Ad": "Ahmet",
    "Sehir": "Istanbul",
    "Yas": 25
}

print("Veri hazırlanıyor...")

# 2. Bunu dosyaya KAYDEDİYORUZ (Write - w)
with open("testing.json", "w", encoding="utf-8") as file:
    json.dump(my_dictionary, file)
    print("✅ File named 'deneme.json' saved!")

# ------------------------------------------------

print("Şimdi dosyadan geri okuyoruz...")

# 3. Dosyadan OKUYORUZ (Read - r)
with open("testing.json", "r", encoding="utf-8") as file:
    reading_data = json.load(file)
    print(f"📂 Data from file: {reading_data}")