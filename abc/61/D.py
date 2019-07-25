def main():
    N, M = map(int, input().split())
    g = []
    INF = 10 ** 9 * 1000
    d = [INF] * (N + 1)
    d[1] = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        g.append((a, b, -c))
    for i in range(2 * N):
        for x, y, z in g:
            if d[x] != INF and d[y] > d[x] + z:
                d[y] = d[x] + z
                if y == N and i > N:
                    print("inf")
                    exit()

    print(-d[-1])


main()
