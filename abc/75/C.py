N, M = map(int, input().split())
G = [[False] * N for _ in range(N)]
A = []
B = []
C = [False] * N
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    A.append(a)
    B.append(b)
    G[a][b] = True
    G[b][a] = True


def dfs(v):
    C[v] = True
    for vv in range(N):
        if G[v][vv] is False:
            continue
        if C[vv] is True:
            continue
        dfs(vv)


def main():
    ans = 0
    for i in range(M):
        G[A[i]][B[i]] = False
        G[B[i]][A[i]] = False
        for j in range(N):
            C[j] = False
        dfs(0)
        G[A[i]][B[i]] = True
        G[B[i]][A[i]] = True
        if all(C) is False:
            ans += 1
            continue
    print(ans)


main()
