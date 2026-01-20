import random
import time

hp = 100
gold = 0
print("--- ⚔️ MINI ADVENTURE STARTS ⚔️ ---")

while True:
    print("\n" + "="*30)
    print(f"❤️  HP: {hp}  |  💰 GOLD: {gold}")
    print("="*30)
    
    if hp <= 0:
        print("💀 You died... Game Over.")
        break

    print("1. 🚪 Open Door (Take Risk)")
    print("2. 💤 Sleep (Heal - Cost: 10 Gold)")
    print("3. 🏃 Exit Game")
    
    choice = input("👉 Your Choice (1-3): ")

    if choice == '1':
        print("Walking into the dark room...")
        time.sleep(1) 
        
        dice = random.randint(1, 10)

        if dice <= 3:
            damage = random.randint(10, 25)
            hp -= damage
            print(f"👹 TRAP! A Goblin attacked you! (-{damage} HP)")
        
        elif dice <= 7:
            print("💨 The room is empty. Just dust and spider webs.")
        
        else:
            loot = random.randint(20, 50)
            gold += loot
            print(f"✨ AWESOME! You found a chest! (+{loot} Gold)")

    elif choice == '2':
        if gold >= 10:
            gold -= 10
            hp += 20
            if hp > 100:

                hp = 100
            print("💤 You slept well. You feel better. (+20 HP)")
        else:
            print("❌ Not enough gold! You cannot stay at the hotel.")

    elif choice == '3':
        print(f"Game Over! Total Gold: {gold}. Congratulations! 🏆")
        break

    else:
        print("⚠️ Please enter 1, 2, or 3.")