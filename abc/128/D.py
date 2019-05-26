def f(s, v, k):
    if k == 0:
        return sum(s)
    v1 = v[::]
    s1 = s[::]
    v2 = v[::]
    s2 = s[::]
    v3 = v[::]
    s3 = s[::]
    s3.append(v3.pop(0))
    v4 = v[::]
    s4 = s[::]
    s4.append(v4.pop(-1))
    a = -1 * (10 ** 7)
    b = -1 * (10 ** 7)
    if len(s) > 0:
        ms = min(s)
        v1.insert(0, ms)
        s1.pop(s1.index(ms))
        v2.append(ms)
        s2.pop(s2.index(ms))
        a = f(s1, v1, k - 1)
        b = f(s2, v2, k - 1)
    c = f(s3, v3, k - 1)
    d = f(s4, v4, k - 1)
    return max(a, b, c, d)


def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = max(f([V[0]], V[1:], K - 1), f([V[-1]], V[:-1], K - 1))
    if ans > 0:
        print(ans)
    else:
        print(0)


main()
