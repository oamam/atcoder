N = int(input())
g = [[] for _ in range(N)]
ans = [[] for _ in range(N - 1)]

def dfs(v, p=-1, c=-1):
    k = 1
    for i in range(len(g[v])):
        u = g[v][i][0]
        e = g[v][i][1]
        if u == p:
            continue
        if k == c:
            k += 1
        ans[e] = k
        k += 1
        dfs(u, v, ans[e])

for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append([b, i])
    g[b].append([a, i])

dfs(0)

mx = 0
for i in range(N):
    mx = max(mx, len(g[i]))
print(mx)
for i in range(N - 1):
    print(ans[i])
