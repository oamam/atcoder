def dfs(i, P):
    if len(P) == N:
        return 1
    c = 0
    for j, v in enumerate(G[i]):
        if j in P or v != 1:
            continue
        c += dfs(j, P + [j])
    return c


N, M = map(int, input().split())
G = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a][b] = 1
    G[b][a] = 1
ans = 0
for i, v in enumerate(G[0]):
    if v == 1:
        ans += dfs(i, [0, i])
print(ans)
