def main():
    N, M = map(int, input().split())
    S = []
    for n in range(N):
        x, y = map(int, input().split())
        S.append((x, y))
    C = []
    for m in range(M):
        x, y = map(int, input().split())
        C.append((x, y))
    ans = []
    for i, s in enumerate(S):
        d = float('INF')
        ans.append(0)
        for j, c in enumerate(C):
            dd = abs(s[0] - c[0]) + abs(s[1] - c[1])
            if d > dd:
                ans[i] = j + 1
                d = dd
    print('\n'.join(map(str, ans)))


main()
