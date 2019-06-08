def main():
    N, Z, W = map(int, input().split())
    a = list(map(int, input().split()))
    i = 0
    tz = Z
    tw = W

    while N > i + 1:
        d = 0
        for j in range(i, N):
            if abs(a[j] - tw) > d:
                d = abs(a[j] - tw)
                tz = a[j]
                i = j + 1
        d = float('INF')
        for k in range(i, N):
            if d > abs(a[k] - tz):
                d = abs(a[k] - tz)
                tw = a[k]
                i = k + 1

    print(max(abs(tz - tw), abs(W - a[-1])))


main()
