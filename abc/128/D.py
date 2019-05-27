def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(K + 1):
        for r in range(K - l + 1):
            if l + r > N:
                continue
            d = K - l - r
            s = V[:l] + V[N - r:N]
            now = 0
            now += sum(s)
            s.sort()
            for i in range(d):
                if i >= len(s):
                    break
                if s[i] > 0:
                    break
                now -= s[i]
            ans = max(ans, now)
    print(ans)


main()
