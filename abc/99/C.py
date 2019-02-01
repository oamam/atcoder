def main():
    N = int(input())
    ans = 0

    while N >= 6:
        i = 0
        j = 0
        while N > 9 ** (i + 1):
            i += 1
        while N > 6 ** (j + 1):
            j += 1
        m = max(9 ** i, 6 ** j)
        print(N, m)
        ans += N // m
        N %= m

    print(ans, N)


main()
