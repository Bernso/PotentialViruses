import os
import random

def create_nested_folders(base_path, depth):
    if depth > 0:
        new_folder = os.path.join(base_path, f"MonkeyCitizen{random.randint(0, 10000000000001)}")
        os.makedirs(new_folder, exist_ok=True)
        create_nested_folders(new_folder, depth - 1)
def main():
    try:
        # Create 50001 levels of nested folders
        for i in range(1, 50001):
            create_nested_folders('MonkeyTown', 500)
            print(f"{i} levels of folders created")
        print("\nFinished creating 50000 levels of nested folders")
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
# lol
