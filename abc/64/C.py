def main():
    _ = int(input())
    A = list(map(int, input().split()))
    c = [False] * (4800 // 400 + 1)
    d = [0] * (4800 // 400 + 1)
    for a in A:
        c[a // 400] = True
        d[a // 400] += 1
    mn = 1 if c[:8].count(True) == 0 else c[:8].count(True)
    mx = c[:8].count(True) + sum(d[8:])
    print(mn, mx)


main()
