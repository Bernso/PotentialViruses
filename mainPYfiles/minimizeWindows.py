import random, pyautogui as pyauto

def main():
#while True:            # To run infinitly
    for i in range(1, 10):
        h = random.randint(0, 1080)             # Just added as random fun
        w = random.randint(0, 1920)             # Just added as random fun  
        pyauto.click(h, w, duration = 0.01)     # Just added as random fun          
        pyauto.hotkey('winleft', 'm')           # The line that actually closes the windows

if __name__ == "__main__":
    main()