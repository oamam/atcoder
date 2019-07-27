def main():
    S = list(input())
    dp = [[0] * 13 for _ in range(10 ** 5 + 1)]
    dp[0][0] = 1
    n = len(S)
    for i in range(n):
        c = 0
        if S[i] == '?':
            c = -1
        else:
            c = int(S[i])
        for si in range(10):
            if c != -1 and c != si:
                continue
            for j in range(13):
                dp[i + 1][(j * 10 + si) % 13] += dp[i][j]
        for j in range(13):
            dp[i + 1][j] %= 10 ** 9 + 7
    print(dp[n][5])


main()
