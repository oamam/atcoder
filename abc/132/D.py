N, K = map(int, input().split())
C = [[0] * (N + 1) for _ in range(N + 1)]
C[0][0] = 1
for i in range(N):
    for j in range(i + 1):
        C[i + 1][j] += C[i][j]
        C[i + 1][j + 1] += C[i][j]


def main():
    for i in range(1, K + 1):
        b = C[N - K + 1][i]
        r = C[K - 1][i - 1]
        ans = b * r % 1000000007
        print(ans)


main()
