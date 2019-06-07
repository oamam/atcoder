def main():
    N, M = map(int, input().split())
    print((M * 1900 + (N - M) * 100) * 2 ** M)


main()
