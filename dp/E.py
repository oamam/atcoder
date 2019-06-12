def main():
    N, W = map(int, input().split())
    Ws = []
    Vs = []
    for _ in range(N):
        w, v = map(int, input().split())
        Ws.append(w)
        Vs.append(v)
    mv = sum(Vs)
    dp = [[float('INF')] * (mv + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(mv + 1):
            if Vs[i] > j:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = min(dp[i][j], dp[i][j - Vs[i]] + Ws[i])
    for j in range(mv, -1, -1):
        if W >= dp[N][j]:
            print(j)
            break


main()
