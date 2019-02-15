def main():
    N, W = map(int, input().split())
    wl = []
    vl = []
    for _ in range(N):
        w, v = map(int, input().split())
        wl.append(w)
        vl.append(v)
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(W + 1):
            if wl[i] > j:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - wl[i]] + vl[i])
    print(dp[N][W])


main()
