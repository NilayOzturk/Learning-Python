import os
from datetime import datetime

# --- SETTINGS ---
FILENAME = "my_diary.txt"

def clear_screen():
    """Clears the terminal screen."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def add_entry():
    """Adds a new entry to the diary file."""
    print("\n--- ✍️ NEW ENTRY ---")
    content = input("Dear Diary: ").strip()
    
    # Get current timestamp (e.g., 2023-10-25 14:30)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Open file in 'append' mode ('a') to add to the end
    try:
        with open(FILENAME, "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] {content}\n")
            file.write("-" * 40 + "\n") # Separator line
        
        print("✅ Entry saved successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    input("\nPress Enter to return...")

def view_entries():
    """Reads and displays all entries from the diary file."""
    print("\n--- 📖 READ DIARY ---")
    
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r", encoding="utf-8") as file:
                data = file.read()
                print(data)
        except Exception as e:
            print(f"❌ Error reading file: {e}")
    else:
        print("📭 The diary is empty.")

    input("\nPress Enter to return...")

def delete_diary():
    """Deletes the diary file."""
    print("\n--- 🗑️ DELETE DIARY ---")
    confirm = input("Are you sure you want to delete all memories? (y/n): ").lower()
    
    if confirm == 'y':
        if os.path.exists(FILENAME):
            os.remove(FILENAME)
            print("✅ Diary deleted successfully.")
        else:
            print("⚠️ File does not exist.")
    else:
        print("❌ Operation cancelled.")
        
    input("\nPress Enter to return...")

# --- MAIN PROGRAM LOOP ---
def main():
    while True:
        clear_screen()
        print("==========================")
        print(" 📔 DIGITAL DIARY v1.0")
        print("==========================")
        print("1. ✍️  Add New Entry")
        print("2. 📖  View All Entries")
        print("3. 🗑️  Delete Diary")
        print("4. 🚪  Exit")
        
        choice = input("\n👉 Select option: ").strip()

        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            delete_diary()
        elif choice == '4':
            print("Goodbye! See you soon. 👋")
            break
        else:
            print("⚠️ Invalid selection. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    import time
    main()