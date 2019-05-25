def main():
    N, M = map(int, input().split())
    A = [0] * (N + 1)
    for _ in range(M):
        L, R = map(int, input().split())
        A[L - 1] += 1
        A[R] -= 1
    c = 0
    ans = 0
    for i, a in enumerate(A):
        c += a
        if c == M:
            ans += 1
    print(ans)


main()
