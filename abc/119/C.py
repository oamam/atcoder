N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]


def f(a, b, c, i):
    if i == N:
        if min(a, b, c) == 0:
            return float('inf')
        return abs(A - a) + abs(B - b) + abs(C - c) - 30
    al = f(a + L[i], b, c, i + 1) + 10
    bl = f(a, b + L[i], c, i + 1) + 10
    cl = f(a, b, c + L[i], i + 1) + 10
    dl = f(a, b, c, i + 1)
    return min(al, bl, cl, dl)


def main():
    print(f(0, 0, 0, 0))


main()
