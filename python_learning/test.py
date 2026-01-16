import os

# 1. Şu an hangi klasördeyiz?
current_folder = os.getcwd()
print(f"📂 Çalışılan Klasör: {current_folder}")

# 2. Bu klasörde hangi dosyalar var?
print("\n--- 📄 Dosyalar ---")
files = os.listdir(current_folder)
for f in files:
    if f.endswith(".json"): # Sadece .json olanları gösterelim
        print(f"Found: {f}")

print("-" * 20)

# 3. Silinecek dosyayı sen yaz (Tam adını yukarıdaki listeden bakarak yaz)
file_to_delete = input("deneme.json").strip()

# 4. Silme İşlemi
if os.path.exists(file_to_delete):
    try:
        os.remove(file_to_delete)
        print(f"✅ BAŞARILI: '{file_to_delete}' silindi!")
    except PermissionError:
        print("❌ HATA: Dosya şu an açık! Lütfen dosyayı kapatıp tekrar dene.")
    except Exception as e:
        print(f"❌ Bir hata oluştu: {e}")
else:
    print(f"❌ HATA: '{file_to_delete}' adında bir dosya bulunamadı.")