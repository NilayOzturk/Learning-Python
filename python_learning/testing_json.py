import json

# 1. Elimizde bir veri var
benim_sozlugum = {
    "Ad": "Ahmet",
    "Sehir": "Istanbul",
    "Yas": 25
}

print("Veri hazırlanıyor...")

# 2. Bunu dosyaya KAYDEDİYORUZ (Write - w)
with open("deneme.json", "w", encoding="utf-8") as dosya:
    json.dump(benim_sozlugum, dosya)
    print("✅ Dosya 'deneme.json' adıyla kaydedildi!")

# ------------------------------------------------

print("Şimdi dosyadan geri okuyoruz...")

# 3. Dosyadan OKUYORUZ (Read - r)
with open("deneme.json", "r", encoding="utf-8") as dosya:
    okunan_veri = json.load(dosya)
    print(f"📂 Dosyadan gelen veri: {okunan_veri}")