H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(10)]
A = [list(map(int, input().split())) for _ in range(H)]


def f(i, s, m):
    if i == 1:
        return s
    a = float('INF')
    for j, k in enumerate(C[i]):
        print(s, a)
        if s >= a:
            print('ok')
            break
        if m[j] is True:
            continue
        m[j] = True
        a = min(a, f(j, s + k, m))
        m[j] = False
    return a


def main():
    ans = 0
    for h in range(H):
        for i in A[h]:
            if i > 1:
                m = [False] * 10
                m[i] = True
                ans += f(i, 0, m)
    print(ans)


main()
