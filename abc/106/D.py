def main():
    N, M, Q = map(int, input().split())
    cs = [[0 for _ in range(N + 1)] for _ in range((N + 1))]
    for _ in range(M):
        L, R = map(int, input().split())
        cs[L][R] += 1
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            cs[i][j] += cs[i - 1][j]
            cs[i][j] += cs[i][j - 1]
            cs[i][j] -= cs[i - 1][j - 1]
    for _ in range(Q):
        p, q = map(int, input().split())
        print(cs[q][q] - cs[q][p - 1] - cs[p - 1][q] + cs[p - 1][p - 1])


main()
