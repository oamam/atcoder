N, Ma, Mb = map(int, input().split())
A = []
B = []
C = []
for _ in range(N):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
M = 401
dp = [[[float('INF') for _ in range(M)]
       for _ in range(M)] for _ in range(N + 1)]
dp[0][0][0] = 0
for i in range(N):
    for j in range(M):
        for k in range(M):
            if dp[i][j][k] == float('INF'):
                continue
            dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
            dp[i + 1][j + A[i]][k + B[i]
                                ] = min(dp[i + 1][j + A[i]][k + B[i]], dp[i][j][k] + C[i])
ans = float('INF')
for j in range(1, M):
    for k in range(1, M):
        if j * Mb == k * Ma:
            ans = min(ans, dp[N][j][k])
if ans == float('INF'):
    print(-1)
else:
    print(ans)
