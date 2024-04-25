import os, random, ctypes

def main():
    folder_path = input("Enter your folder path: ")
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]

    if not image_files:
        print("No image files found in the folder.")
        return

    image_file = random.choice(image_files)
    image_path = os.path.join(folder_path, image_file)

    # Check the operating sys
    if os.name == 'nt':  # For Windows systems
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        print("Wallpaper changed successfully.")
    elif os.name == 'posix':  # For Linux 
        os.system(f"feh --bg-scale {image_path}")
        print("Wallpaper changed successfully.")
    else:
        print("Unsupported operating system.")

if __name__ == "__main__":
    main()
