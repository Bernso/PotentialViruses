import requests

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
if __name__ == "__main__":
    get_public_ip()
