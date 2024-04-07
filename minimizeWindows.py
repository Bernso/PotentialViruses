import random, pyautogui as pyauto

def main():
#while True:            # To run infinitly
    for i in range(1, 10):
        h = random.randint(0, 1080)
        w = random.randint(0, 1920)
        pyauto.click(h, w, duration = 0.01)
        pyauto.hotkey('winleft', 'm')

if __name__ == "__main__":
    main()