import os

# Silmek istediğin dosyanın tam adını buraya yaz
file_to_delete = "deneme.json" 

if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f"🗑️ {file_to_delete} has been deleted successfully.")
else:
    print("❌ File does not exist.")
