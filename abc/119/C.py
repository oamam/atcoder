N, A, B, C = map(int, input().split())


def f(a, b, c, bl, ans):
    if len(bl) == 0:
        if len(a) == 0 or len(b) == 0 or len(c) == 0:
            return ans
        return abs(A - sum(a)) + (len(a) - 1) * 10 + \
            abs(B - sum(b)) + (len(b) - 1) * 10 + \
            abs(C - sum(c)) + (len(c) - 1) * 10
    for i in range(len(bl)):
        l = bl[i]
        a.append(l)
        ans = min(ans, f(a, b, c, bl[i + 1:], ans))
        a.pop(-1)
        b.append(l)
        ans = min(ans, f(a, b, c, bl[i + 1:], ans))
        b.pop(-1)
        c.append(l)
        ans = min(ans, f(a, b, c, bl[i + 1:], ans))
        c.pop(-1)
        ans = min(ans, f(a, b, c, bl[i + 1:], ans))
    return ans


def main():
    bl = []
    for _ in range(N):
        bl.append(int(input()))
    print(f([], [], [], bl, 10000))


main()
