D, G = map(int, input().split())
PC = [[int(pc) for pc in input().split()] for _ in range(D)]


def f(d, g):
    if 0 > d:
        return 100 ** 10
    n = min(g // (100 * (d + 1)), PC[d][0])
    s = n * 100 * (d + 1)
    if n == PC[d][0]:
        s += PC[d][1]
    if g > s:
        n += f(d - 1, g - s)
    return min(n, f(d - 1, g))


def main():
    print(f(D - 1, G))


main()
