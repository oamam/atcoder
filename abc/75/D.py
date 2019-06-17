def main():
    N, K = map(int, input().split())
    X = []
    Y = []
    XY = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
        XY.append((x, y))
    X.sort()
    Y.sort()

    ans = float('INF')
    for l in range(N):
        for r in range(l + 1, N):
            for d in range(N):
                for t in range(d + 1, N):
                    lx = X[l]
                    rx = X[r]
                    ty = Y[t]
                    dy = Y[d]
                    c = 0
                    for x, y in XY:
                        if lx <= x <= rx and dy <= y <= ty:
                            c += 1
                    if c >= K:
                        ans = min(ans, abs(rx - lx) * abs(ty - dy))
    print(ans)


main()
