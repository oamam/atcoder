def main():
    N, W = map(int, input().split())
    MV = 10**5
    dp = [float('INF')] * (MV + 1)
    dp[0] = 0
    for _ in range(N):
        w, v = map(int, input().split())
        for i in range(MV, -1, -1):
            if v > i:
                tmp = w
            else:
                tmp = dp[i - v] + w
            dp[i] = min(dp[i], tmp)
    ans = 0
    for v, w in enumerate(dp):
        if W >= w:
            ans = max(ans, v)
        else:
            break
    print(ans)


main()
