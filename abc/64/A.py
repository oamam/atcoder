def main():
    r, g, b = input().split()
    print('YNEOS'[int(r + g + b) % 4 != 0::2])


main()
