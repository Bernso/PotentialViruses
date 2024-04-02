import os
import random

def create_nested_folders(base_path, depth):
    if depth > 0:
        new_folder = os.path.join(base_path, f"Folder_{random.randint(0, 10000000000001)}")
        os.makedirs(new_folder, exist_ok=True)
        create_nested_folders(new_folder, depth - 1)
try:
    # Example usage: Create 5 levels of nested folders
    for i in range(1, 50001):
        create_nested_folders('BaseFolder', 500)
        print(f"{i} levels of folders created")
except Exception as e:
    print(f"Error: {e}")
# lol
