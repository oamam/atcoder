import bisect


def f(a, x):
    i = bisect.bisect_left(a, x)
    if 0 >= i:
        return a[0]
    if i >= len(a):
        return a[-1]
    if x - a[i - 1] > a[i] - x:
        return a[i]
    return a[i - 1]


def main():
    A, B, Q = map(int, input().split())
    s = [-float('inf')]
    t = [-float('inf')]
    ans = []
    for _ in range(A):
        s.append(int(input()))
    for _ in range(B):
        t.append(int(input()))
    s.append(float('inf'))
    t.append(float('inf'))
    for _ in range(Q):
        x = int(input())
        i = bisect.bisect_right(s, x)
        j = bisect.bisect_right(t, x)
        a = float('inf')
        for ss in [s[i - 1], s[i]]:
            for tt in [t[j - 1], t[j]]:
                a = min(a, abs(ss - x) + abs(tt - ss),
                        abs(tt - x) + abs(ss - tt))
        ans.append(a)
    for a in ans:
        print(a)


main()
