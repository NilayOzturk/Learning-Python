import random
import time

# --- INITIAL SETTINGS (Başlangıç Ayarları) ---
hp = 100
gold = 0
print("--- ⚔️ MINI ADVENTURE STARTS ⚔️ ---")

# --- GAME LOOP (Oyun Döngüsü) ---
while True:
    print("\n" + "="*30)
    print(f"❤️  HP: {hp}  |  💰 GOLD: {gold}")
    print("="*30)
    
    # Check if dead (Ölüm Kontrolü)
    if hp <= 0:
        print("💀 You died... Game Over.")
        break

    print("1. 🚪 Open Door (Take Risk)")
    print("2. 💤 Sleep (Heal - Cost: 10 Gold)")
    print("3. 🏃 Exit Game")
    
    choice = input("👉 Your Choice (1-3): ")

    # --- OPTION 1: TAKE RISK (Risk Al) ---
    if choice == '1':
        print("Walking into the dark room...")
        time.sleep(1) 
        
        dice = random.randint(1, 10) # 1-10 arası zar at

        if dice <= 3: # 30% Monster (Canavar)
            damage = random.randint(10, 25)
            hp -= damage
            print(f"👹 TRAP! A Goblin attacked you! (-{damage} HP)")
        
        elif dice <= 7: # 40% Empty (Boş)
            print("💨 The room is empty. Just dust and spider webs.")
        
        else: # 30% Treasure (Hazine)
            loot = random.randint(20, 50) # loot = ganimet
            gold += loot
            print(f"✨ AWESOME! You found a chest! (+{loot} Gold)")

    # --- OPTION 2: SLEEP (Uyu) ---
    elif choice == '2':
        if gold >= 10:
            gold -= 10
            hp += 20
            # Limit HP to 100 (Can 100'ü geçmesin)
            if hp > 100:
                hp = 100
            print("💤 You slept well. You feel better. (+20 HP)")
        else:
            print("❌ Not enough gold! You cannot stay at the hotel.")

    # --- OPTION 3: EXIT (Çıkış) ---
    elif choice == '3':
        print(f"Game Over! Total Gold: {gold}. Congratulations! 🏆")
        break

    else:
        print("⚠️ Please enter 1, 2, or 3.")