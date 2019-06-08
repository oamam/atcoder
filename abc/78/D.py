def main():
    N, Z, W = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = max(abs(a[i] - W), abs(a[i - 1] - a[i]))
    print(dp[-1])


main()
