def main():
    a, b, c, d = input()
    print('YNeos'[not (a == b == c or b == c == d)::2])


main()
