def main():
    N, X = map(int, input().split())
    dx = [abs(X - x) for x in map(int, input().split())]
    if N == 1:
        ans = dx[0]
    else:
        ans = 10 ** 9
    for i in range(N - 1):
        nm = dx[i]
        dm = dx[i + 1]
        while True:
            mod = nm % dm
            if mod == 0:
                break
            nm = dm
            dm = mod
        ans = min(ans, dm)
    print(ans)


main()
