import subprocess

def get_hwid():
    # Run the Windows Management Instrumentation Command-line (WMIC) to get the UUID
    hwid = subprocess.check_output('wmic csproduct get uuid', shell=True).decode().split('\n')[1].strip()
    print(f"The HWID of this machine is: {hwid}")
if __name__ == '__main__':
    get_hwid()
