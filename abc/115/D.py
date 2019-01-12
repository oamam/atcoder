N, X = list(map(int, input().split()))
a, p = [1], [1]
for i in range(N):
    a.append(a[i] * 2 + 3)
    p.append(p[i] * 2 + 1)


def check(n, x):
    if n == 0:
        if x <= 0:
            return 0
        else:
            return 1

    if x <= 1 + a[n - 1]:
        return check(n - 1, x - 1)

    return p[n - 1] + 1 + check(n - 1, x - 2 - a[n - 1])


def main():
    print(check(N, X))


if __name__ == '__main__':
    main()
