N, M = map(int, input().split())
g = [[float('INF')] * (N + 1) for _ in range(N + 1)]
abc = []
for _ in range(M):
    a, b, c = map(int, input().split())
    abc.append((a, b, c))
    g[a][b] = c
    g[b][a] = c
for k in range(N + 1):
    for i in range(N + 1):
        for j in range(N + 1):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])
ans = 0
for a, b, c in abc:
    if g[a][b] != c:
        ans += 1
print(ans)
