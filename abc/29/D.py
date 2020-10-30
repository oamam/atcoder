P = 10**9 + 7
N = input()
n = list(map(int, list(N)))
l = len(n)
dp = [[[0] * 11 for _ in range(2)] for _ in range(l + 1)]
dp[0][0][0] = 1
for i in range(l):
    m = n[i]
    for j in range(10):
        dp[i + 1][1][j] += dp[i][1][j] * 9
        dp[i + 1][1][j + 1] += dp[i][1][j]
        
        if (m > 1):
            dp[i + 1][1][j] += dp[i][0][j] * (m - 1)
            dp[i + 1][1][j + 1] += dp[i][0][j]
        elif (m == 1):
            dp[i + 1][1][j] += dp[i][0][j]

        if (m == 1):
            dp[i + 1][0][j + 1] += dp[i][0][j]
        else:
            dp[i + 1][0][j] += dp[i][0][j]
ans = 0
for j in range(10):
    ans += ((dp[l][0][j] + dp[l][1][j]) * j) % P
print(ans)