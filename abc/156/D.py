def fact(n, k, mod):
    res = 1
    for i in range(k):
        res = res * (n - i) % mod
    return res

def c(x, y, mod):
    y = min(y, x - y)
    return (fact(x, y, mod) * pow(fact(y, y, mod), mod - 2, mod)) % mod

P = 10**9 + 7
n, a, b = map(int, input().split())
print((pow(2, n, P) - 1 - c(n, a, P) - c(n, b, P)) % P)