def main():
    n = int(input())
    v = list(map(int, input().split()))
    e = [0 for _ in range(1, 10 ** 5 + 2)]
    o = [0 for _ in range(1, 10 ** 5 + 2)]
    for i in range(0, n, 2):
        e[v[i]] += 1
        o[v[i + 1]] += 1
    ans = 0
    if len(set(v)) == 1:
        ans = n // 2
    else:
        me = max(e)
        mo = max(o)
        mei = e.index(me)
        moi = o.index(mo)
        if mei == moi:
            e[mei] = 0
            o[moi] = 0
            ans += n - me - max(max(e), max(o))
        else:
            ans = n - max(e) - max(o)
    print(ans)


main()
