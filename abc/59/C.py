n = int(input())
a = list(map(int, input().split()))


def f(p):
    sa = 0
    ans = 0
    for ai in a:
        if p:
            sa += ai
            if sa >= 0:
                ans += sa + 1
                sa = -1
            p = False
        else:
            sa += ai
            if 0 >= sa:
                ans += 1 - sa
                sa = 1
            p = True
    return ans


def main():
    print(min(f(True), f(False)))


main()
