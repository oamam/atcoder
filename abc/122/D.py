def main():
    N = int(input())
    dp = [[[[0 for _ in range(4)] for _ in range(4)]
           for _ in range(4)] for _ in range(101)]
    dp[0][3][3][3] = 1
    mod = 1_000_000_007
    for n in range(100):
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if dp[n][i][j][k] == 0:
                        continue
                    for a in range(4):
                        if (j == 0 and i == 1 and a == 2) or \
                            (j == 0 and i == 2 and a == 1) or \
                            (j == 1 and i == 0 and a == 2) or \
                            (k == 0 and j == 1 and a == 2) or \
                                (k == 0 and i == 1 and a == 2):
                            continue
                        dp[n + 1][a][i][j] += dp[n][i][j][k]
                        dp[n + 1][a][i][j] %= mod
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[N][i][j][k]
                ans %= mod
    print(ans)


main()
