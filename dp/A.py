def main():
    N = int(input())
    h = list(map(int, input().split()))
    dp = [0 for _ in range(N)]
    dp[1] = abs(h[0] - h[1])
    for i in range(2, N):
        h1 = dp[i - 1] + abs(h[i] - h[i - 1])
        h2 = dp[i - 2] + abs(h[i] - h[i - 2])
        dp[i] = min(h1, h2)

    print(dp[-1])


main()
