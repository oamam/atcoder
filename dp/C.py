def main():
    N = int(input())
    a = [0]
    b = [0]
    c = [0]
    for _ in range(N):
        ai, bi, ci = map(int, input().split())
        a.append(ai)
        b.append(bi)
        c.append(ci)
    dp = [[0] * 3 for _ in range(N + 1)]

    for i in range(1, N + 1):
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + a[i]
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + b[i]
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + c[i]

    print(max(dp[N]))


main()
