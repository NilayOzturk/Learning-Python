import json
import os   # ✨ YENİ OYUNCU: İşletim Sistemi ile konuşur
import time # Biraz bekleme efekti için

# --- AYARLAR ---
FILENAME = "todo_list.json"

# --- OS SİHİRLERİ (OS MAGIC) ---

def clean_screen():
    """Terminal ekranını temizler (Silgi görevi görür)."""
    # Windows kullanıyorsan 'cls', Mac/Linux ise 'clear' komutunu çalıştırır.
    # os.name == 'nt' demek "Windows" demektir.
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def check_file_exists():
    """Dosyanın var olup olmadığını kontrol eder."""
    # os.path.exists -> "Hey bilgisayar, bu klasörde böyle bir dosya var mı?"
    return os.path.exists(FILENAME)

# --- JSON İŞLEMLERİ (VERİTABANI) ---

def load_tasks():
    if check_file_exists(): # Önce os ile kontrol et!
        try:
            with open(FILENAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except:
            return [] # Dosya bozuksa boş liste dön
    else:
        return [] # Dosya yoksa boş liste dön

def save_tasks(tasks):
    try:
        with open(FILENAME, "w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Hata oluştu: {e}")

# --- ANA PROGRAM ---

def main():
    my_tasks = load_tasks()

    while True:
        clean_screen() # ✨ HER TURDA EKRANI TEMİZLE!
        
        print("--- 📝 YAPILACAKLAR LİSTESİ / TO-DO LIST ---")
        print(f"Toplam Görev: {len(my_tasks)}\n")

        # Görevleri Listele
        # enumerate -> Hem sıra numarasını (i) hem görevi (task) verir
        for i, task in enumerate(my_tasks, 1):
            print(f"{i}. {task}")
        
        print("\n" + "-"*30)
        print("1. ➕ Görev Ekle (Add Task)")
        print("2. 🗑️ Görev Sil (Delete Task)")
        print("3. ❌ Çıkış (Exit)")
        
        choice = input("\n👉 Seçimin: ").strip()

        if choice == '1':
            new_task = input("Yapılacak iş nedir?: ").strip()
            if new_task:
                my_tasks.append(new_task)
                save_tasks(my_tasks)
                print("✅ Eklendi!")
                time.sleep(1) # Yazıyı okuyabilsin diye 1 sn bekle

        elif choice == '2':
            try:
                task_num = int(input("Silinecek numara: "))
                # Listeden sil (pop komutu index ile siler, o yüzden -1 yapıyoruz)
                silinen = my_tasks.pop(task_num - 1)
                save_tasks(my_tasks)
                print(f"🗑️ '{silinen}' silindi!")
                time.sleep(1)
            except:
                print("⚠️ Hatalı numara girdin!")
                time.sleep(1)

        elif choice == '3':
            print("Görüşürüz! 👋")
            break

if __name__ == "__main__":
    main()