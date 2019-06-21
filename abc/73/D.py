N, M, R = map(int, input().split())
T = list(map(int, input().split()))
D = [[float('INF')] * N for _ in range(N)]
V = [False] * R
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    if D[A][B] > C:
        D[A][B] = C
        D[B][A] = C
ans = float('INF')


def dfs(c, s, d):
    global ans
    if c == R:
        ans = max(ans, d)
        return
    for i in range(R):
        if V[i] is True:
            continue
        V[i] = True
        if s == -1:
            dfs(c + 1, i, 0)
        else:
            dfs(c + 1, i, d + D[T[s] - 1][T[i] - 1])
        V[i] = False


def main():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    dfs(0, -1, 0)
    print(ans)


main()
