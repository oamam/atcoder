def main():
    N, W = map(int, input().split())
    wv = {0: 0}
    for _ in range(N):
        w, v = map(int, input().split())
        kw = sorted(list(wv.keys()), reverse=True)
        for k in kw:
            if k + w not in wv:
                wv[k + w] = wv[k] + v
            else:
                wv[k + w] = max(wv[k + w], wv[k] + v)
    kw = sorted(list(wv.keys()))
    ans = 0
    for k in kw:
        if k > W:
            break
        ans = max(ans, wv[k])
    print(ans)


main()
