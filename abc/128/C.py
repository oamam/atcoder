def main():
    N, M = map(int, input().split())
    A = [0] * N
    for i in range(M):
        for s in list(map(int, input().split()))[1:]:
            A[s - 1] |= 1 << i
    p = 0
    for i, j in enumerate(list(map(int, input().split()))):
        p |= j << i
    ans = 0
    for s in range(1 << N):
        t = 0
        for i in range(N):
            if s >> i & 1:
                t ^= A[i]
        if t == p:
            ans += 1
    print(ans)


main()
