def main():
    N, M = list(map(int, input().split()))

    pref = []
    for _ in range(M):
        P, Y = list(map(int, input().split()))
        pref.append((P, Y))

    pref_sorted = sorted(enumerate(pref), key=lambda x: x[1])

    idx = [1 for _ in range(N)]
    res = ['' for _ in range(M)]
    for j, (p, y) in pref_sorted:
        res[j] = str(p).zfill(6) + str(idx[p - 1]).zfill(6)
        idx[p - 1] += 1
    for r in res:
        print(r)


if __name__ == '__main__':
    main()
