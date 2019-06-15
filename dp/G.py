def main():
    N, M = map(int, input().split())
    E = [[] for _ in range(N + 1)]
    D = [0] * (N + 1)
    for _ in range(M):
        x, y = map(int, input().split())
        E[x].append(y)
        # Keeps number of input destinations for each output distination.
        D[y] += 1

    # topological sort
    Q = [i for i in range(1, N + 1) if D[i] == 0]
    L = []
    while Q:
        s = Q.pop()
        L.append(s)
        for r in E[s]:
            D[r] -= 1
            if D[r] == 0:
                Q.append(r)

    dp = [0] * (N + 1)
    for v in L:
        c = dp[v] + 1
        for k in E[v]:
            dp[k] = max(dp[k], c)
    print(max(dp))


main()
