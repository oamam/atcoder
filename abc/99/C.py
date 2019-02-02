def main():
    N = int(input())
    dp = [N] * (N + 1)
    dp[0] = 0
    for n in range(1, N + 1):
        i = 1
        while n >= i:
            dp[n] = min(dp[n], dp[n - i] + 1)
            i *= 6
        j = 1
        while n >= j:
            dp[n] = min(dp[n], dp[n - j] + 1)
            j *= 9
    print(dp[N])


main()
