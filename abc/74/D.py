def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        A[i][i] = float('INF')
    for i in range(N):
        for j in range(i):
            b = min(map(sum, zip(A[i], A[j])))
            if A[i][j] > b:
                print(-1)
                return
            if b > A[i][j]:
                ans += A[i][j]
    print(ans)


main()
