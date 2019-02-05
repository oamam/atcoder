def main():
    H, W = map(int, input().split())
    s = [list(input()) for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if s[h][w] != '#':
                continue
            flg = False
            for dh, dw in zip([-1, 0, 0, 1], [0, -1, 1, 0]):
                if h + dh >= 0 and H > h + dh and \
                    w + dw >= 0 and W > w + dw and \
                        s[h + dh][w + dw] == '#':
                    flg = True
                    break
            if flg is False:
                print('No')
                exit()

    print('Yes')


main()
