def main():
    N, M, Q = map(int, input().split())
    LR = [[0 for _ in range(N + 1)] for _ in range((N + 1))]
    for _ in range(M):
        L, R = map(int, input().split())
        LR[L][R] += 1
    ans = []
    for _ in range(Q):
        p, q = map(int, input().split())
        c = 0
        for R in LR[p:]:
            c += sum(R[:q + 1])
        ans.append(c)
    for a in ans:
        print(a)


main()
