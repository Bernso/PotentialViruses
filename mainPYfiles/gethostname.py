import socket

def get_computer_name():
    computer_name = socket.gethostname()
    print(f"\nThe computers name is: {computer_name}")

if __name__ == '__main__':
    get_computer_name()