def amida(h, w, k, n):
    if w == 1:
        if k == 1:
            return 1
        else:
            return 0
    if h == 0:
        if n == k:
            return 1
        else:
            return 0
    cnt = 0
    if n == 1:
        cnt += amida(h - 1, w, k, n + 1)
        cnt += amida(h - 1, w, k, n) * (w - 1)
    elif w == n:
        cnt += amida(h - 1, w, k, n - 1)
        cnt += amida(h - 1, w, k, n) * (w - 1)
    else:
        cnt += amida(h - 1, w, k, n + 1)
        cnt += amida(h - 1, w, k, n - 1)
        cnt += amida(h - 1, w, k, n) * (w - 2)

    return cnt


def main():
    H, W, K = list(map(int, input().split()))
    print(amida(H, W, K, 1) % 1000000007)


if __name__ == '__main__':
    main()
