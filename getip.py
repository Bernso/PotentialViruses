import requests
import socket



def get_private_ip():
    # Get the hostname
    hostname = socket.gethostname()

    # Get the private IP address
    private_ip = socket.gethostbyname(hostname)
   
    print(f"\nYour private IP Address is: {private_ip}")

def get_computer_name():
    computer_name = socket.gethostname()
    print(f"Your computers name is: {computer_name}")


def get_public_ip():
    try:
        # Make a request to an external service that echoes back the requester's IP address
        response = requests.get('https://api.ipify.org?format=json')
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response and extract the IP address
            ip_address = response.json()['ip']
            print(f"Your public IP address is: {ip_address}")
        else:
            print(f"Failed to retrieve IP address. Status code: {response.status_code}")
            
    except Exception as e:
        print(f"An error occurred: {e}")
        
def user_choice():
    choice = input("\nWhat would you like? (priv/pub/name/all)\n")
    if choice.lower() == "priv":
        get_private_ip()
    elif choice.lower() == "pub":
        get_public_ip()
    elif choice.lower() == "name":
        get_computer_name()
    elif choice.lower() == "all":
        get_private_ip()
        get_computer_name()
        get_public_ip()
        print("Your IP's have been printed above ^\n")
    else:
        print("\nPlease enter a valid option.")
        print("Bro fr doesn't know how to spell lmao")
        user_choice()
        
        

if __name__ == "__main__":
    user_choice()
