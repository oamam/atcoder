def main():
    N, K = map(int, input().split())
    M = (N - 1) * (N - 2) // 2
    if K > M:
        print(-1)
        return
    ans = []
    for i in range(N - 1):
        ans.append((i + 1, N))
    E = []
    for i in range(N - 1):
        for j in range(i):
            E.append((i + 1, j + 1))
    for i in range(M - K):
        ans.append(E[i])
    print(len(ans))
    for i, j in ans:
        print(i, j)


main()
