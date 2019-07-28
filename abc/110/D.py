mod = 1000000007


def modpow(a, p):
    if p == 0:
        return 1
    if p % 2 == 0:
        h = modpow(a, p // 2)
        return h * h % mod
    else:
        return a * modpow(a, p - 1) % mod


def calc(a, b):
    if b > a - b:
        return calc(a, a - b)
    am = 1
    ad = 1
    for i in range(b):
        am *= (a - i)
        ad *= (i + 1)
        am %= mod
        ad %= mod
    return am * modpow(ad, mod - 2) % mod


def main():
    N, M = map(int, input().split())
    res = M
    ans = 1
    i = 2
    while res >= i * i:
        if res % i == 0:
            c = 0
            while res % i == 0:
                c += 1
                res //= i
            ans *= calc(N + c - 1, N - 1)
            ans %= mod
        i += 1
    if res != 1:
        ans *= calc(N, N - 1)
        ans %= mod
    print(ans)


main()
