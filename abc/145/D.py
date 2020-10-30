def fact(n, k, mod):
    res = 1
    for i in range(k):
        res = res * (n - i) % mod
    return res

def c(x, y, mod):
    y = min(x, x - y)
    return (fact(x, y, mod) * pow(fact(y, y, mod), mod - 2 , mod)) % mod

P = 10**9 + 7
X, Y = map(int, input().split())
if (X + Y) % 3 > 0:
    print(0)
    exit()
n = (X + Y) // 3
x = X - n
y = Y - n
if 0 > x or 0 > y:
    print(0)
    exit()
print(c(x + y, x, P))