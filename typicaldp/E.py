P = 10**9 + 7
D = int(input())
N = input()
n = list(map(int, list(N)))
l = len(n)
dp = [[0] * D for _ in range(2)]
dp[0][0] = 1
for i in range(l):
    m = n[i]
    t_dp = [[0] * D for _ in range(2)]
    for s in range(2):
        for j in range(D):
            for x in range(10 if s else m + 1):
                t_dp[s or x < m][(j + x) % D] += dp[s][j]
                t_dp[s or x < m][(j + x) % D] %= P
    dp = t_dp[::]
print(dp[0][0] + dp[1][0] - 1)