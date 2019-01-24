def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))

    i = 0
    ans = 10 ** 8 * n
    while i < n - k + 1:
        lr = abs(x[i]) + abs(x[i] - x[i + k - 1])
        rl = abs(x[i + k - 1]) + abs(x[i] - x[i + k - 1])
        i += 1
        ans = min(ans, lr, rl)
    print(ans)


main()
