def main():
    N = input()
    print('YNeos'[not int(N) % sum(int(n) for n in N) == 0::2])


main()
