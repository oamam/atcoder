def main():
    N, A, B = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    left = 1
    right = max(H)
    while right - left > 1:
        t = (right + left) // 2
        c = 0
        for h in H:
            x = h - B * t
            if 0 >= x:
                continue
            c += x // (A - B)
            if x % (A - B):
                c += 1
        if c > t:
            left = t
        else:
            right = t
    print(right)


main()
