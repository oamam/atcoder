N = int(input())
e = [0] * (N + 1)
for i in range(2, N + 1):
    c = i
    for j in range(2, i + 1):
        while c % j == 0:
            e[j] += 1
            c //= j


def fn(m):
    return len(list(filter(lambda x: x >= m - 1, e)))


print(
    fn(75) +
    fn(25) * (fn(3) - 1) +
    fn(15) * (fn(5) - 1) +
    fn(5) * (fn(5) - 1) * (fn(3) - 2) // 2
)
