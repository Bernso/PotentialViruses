import time, rotatescreen as rs
def main():
    pd = rs.get_primary_display()
    pd.rotate_to(0)


if __name__ == '__main__':
    main()