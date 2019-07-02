def main():
    H, W = map(int, input().split())
    N = int(input())
    A = list(map(int, input().split()))
    ans = [[0] * W for _ in range(H)]
    i = 0
    j = 0
    d = 1
    for n in range(N):
        for _ in range(A[n]):
            ans[i][j] = str(n + 1)
            if (0 > d and j == 0) or (d > 0 and j == W - 1):
                i += 1
                d *= -1
                continue
            j += d
    for r in ans:
        print(' '.join(r))


main()
