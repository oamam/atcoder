def main():
    N, M = map(int, input().split())
    A = [0] * (N + 1)
    for _ in range(M):
        A[int(input())] = 1
    dp = [0] * (N + 2)
    dp[-2] = 1
    for i in range(N - 1, -1, -1):
        if A[i] == 1:
            continue
        dp[i] = dp[i + 1] + dp[i + 2]
    print(dp[0] % 1000000007)


main()
