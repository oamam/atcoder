def main():
    N, M = map(int, input().split())
    switchs = []
    for _ in range(M):
        ks = list(map(int, input().split()))
        switchs.append([1 << s - 1 for s in ks[1:]])
    p = list(map(int, input().split()))
    ans = 0
    for b in range(1 << N):
        f = True
        for i, s in enumerate(switchs):
            c = 0
            for ss in s:
                if b & ss:
                    c += 1
            if c % 2 != p[i]:
                f = False
                break
        if f:
            ans += 1
    print(ans)

main()