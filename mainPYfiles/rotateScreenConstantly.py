import time, rotatescreen as rs

def main():
    pd = rs.get_primary_display()
    angles = [0, 90, 180, 270]
    #while True:       #To make it never stop :)
    for i in range(0, len(angles)):
        for x in angles:
            pd.rotate_to(x)
            time.sleep(0.5)

# 4 x 4 = 16
# rotates the screen 16 times

if __name__ == '__main__':
    main()