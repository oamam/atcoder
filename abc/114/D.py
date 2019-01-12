def check(m, e):
    return len(list(filter(lambda x: x >= m - 1, e)))


def main():
    N = int(input())
    e = [0] * (N + 1)

    for i in range(2, N + 1):
        ii = i
        for j in range(2, i + 1):
            while ii % j == 0:
                e[j] += 1
                ii //= j

    print(check(75, e) +
          check(25, e) * (check(3, e) - 1) +
          check(15, e) * (check(5, e) - 1) +
          check(5, e) * (check(5, e) - 1) * (check(3, e) - 2) // 2)


if __name__ == '__main__':
    main()
