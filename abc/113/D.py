def main():
    H, W, K = list(map(int, input().split()))
    dp = [[0 for _ in range(W)] for _ in range(H + 1)]
    dp[0][0] = 1

    for i in range(H):
        for j in range(1 << (W - 1)):
            if '11' in bin(j):
                continue
            j <<= 1
            for k in range(W):
                if j & (1 << k):
                    dp[i + 1][k] += dp[i][k - 1]
                elif j & (1 << (k + 1)):
                    dp[i + 1][k] += dp[i][k + 1]
                else:
                    dp[i + 1][k] += dp[i][k]
                dp[i + 1][k] %= (10 ** 9 + 7)
    print(dp[H][K - 1])


if __name__ == '__main__':
    main()
