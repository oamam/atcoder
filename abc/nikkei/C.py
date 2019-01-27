def main():
    N = int(input())
    a = []
    b = []
    for _ in range(N):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = 0
    s = 1
    while True:
        if sum(a) == 0:
            print(ans)
            exit()
        ma = max(a)
        mb = max(b)
        ans += ma * s
        if ma >= mb:
            i = a.index(ma)
        else:
            i = b.index(mb)
        a[i] = 0
        b[i] = 0
        t = a
        a = b
        b = t
        s *= -1


main()
