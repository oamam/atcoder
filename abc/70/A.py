def main():
    N = input()
    print('YNeos'[not N == N[::-1]::2])


main()
