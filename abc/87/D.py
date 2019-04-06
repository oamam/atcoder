def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    D = [-1 for _ in range(N)]
    E = [0 for _ in range(N)]
    for _ in range(M):
        l, r, d = map(int, input().split())
        G[l - 1].append((r - 1, d))
        E[r - 1] = 1
    for i in range(N):
        if E[i] == 1:
            continue
        s = [i]
        while len(s) > 0:
            ll = s.pop()
            for rr, dd in G[ll]:
                if D[rr] == -1:
                    D[rr] = D[ll] + dd
                    s.append(rr)
    for l in range(N):
        for r, d in G[l]:
            if D[l] + d != D[r]:
                print('No')
                return
    print('Yes')


main()
