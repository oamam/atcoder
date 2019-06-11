def main():
    N, W = map(int, input().split())
    WV = []
    for _ in range(N):
        w, v = map(int, input().split())
        WV.append((w, v))
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(W + 1):
            if j >= WV[i][0]:
                dp[i + 1][j] = max(
                    dp[i][j],
                    dp[i][j - WV[i][0]] + WV[i][1]
                )
            else:
                dp[i + 1][j] = dp[i][j]
    print(dp[-1][-1])


main()
