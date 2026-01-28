import os
import datetime  # 📅 YENİ: Tarih ve saat işlemleri için

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def write_entry():
    """Kullanıcıdan not alır ve dosyaya ekler."""
    print("\n--- ✍️ WRITE NEW ENTRY ---")
    text = input("Dear Diary: ")
    
    # Şu anki zamanı alalım (Örn: 2023-10-27 15:30)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # 📝 ÖNEMLİ: "a" (append) modu kullanıyoruz.
    # "w" yapsaydık eskileri silerdi. "a" ise SONA EKLER.
    with open("diary.txt", "a", encoding="utf-8") as file:
        file.write(f"[{current_time}] {text}\n")
        
    print("✅ Saved to diary.txt!")
    input("Press Enter to continue...")

def read_entries():
    """Eski notları okur."""
    print("\n--- 📖 READ DIARY ---")
    
    if os.path.exists("diary.txt"):
        with open("diary.txt", "r", encoding="utf-8") as file:
            content = file.read()
            print(content)
    else:
        print("📭 Diary is empty yet.")
    
    input("\nPress Enter to continue...")

# --- MAIN PROGRAM ---
while True:
    clear_screen()
    print("📔 MY PERSONAL DIARY")
    print("1. ✍️ Write New Entry")
    print("2. 📖 Read Old Entries")
    print("3. ❌ Exit")
    
    choice = input("👉 Choice: ")

    if choice == '1':
        write_entry()
    elif choice == '2':
        read_entries()
    elif choice == '3':
        print("Goodbye! See you tomorrow. 👋")
        break
    else:
        print("Invalid choice!")