import socket


def get_private_ip():
    # Get the hostname
    hostname = socket.gethostname()

    # Get the private IP address
    private_ip = socket.gethostbyname(hostname)
   
    print(f"\nYour private IP Address is: {private_ip}")

if __name__ == '__main__':
    get_private_ip()