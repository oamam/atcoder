N, X = map(int, input().split())
a = [1]
p = [1]
for i in range(N):
    a.append(a[i] * 2 + 3)
    p.append(p[i] * 2 + 1)


def f(n, x):
    if n == 0:
        return 1
    if x == 1:
        return 0
    if 1 < x <= a[n - 1] + 1:
        return f(n - 1, x - 1)
    if x == a[n - 1] + 2:
        return p[n - 1] + 1
    if a[n - 1] + 2 < x <= 2 * a[n - 1] + 2:
        return p[n - 1] + 1 + f(n - 1, x - 2 - a[n - 1])
    if x == 2 * a[n - 1] + 3:
        return 2 * p[n - 1] + 1


print(f(N, X))
