def main():
    H, W = map(int, input().split())
    s = [list(input()) for _ in range(H)]
    if s[0][0] == '#':
        if s[1][0] != '#' and \
                s[0][1] != '#':
            print('No')
            exit()
    if s[H - 1][0] == '#':
        if s[H - 2][0] != '#' and \
                s[H - 1][1] != '#':
            print('No')
            exit()
    if s[0][W - 1] == '#':
        if s[0][W - 2] != '#' and \
                s[1][W - 1] != '#':
            print('No')
            exit()
    if s[H - 1][W - 1] == '#':
        if s[H - 2][W - 1] != '#' and \
                s[H - 1][W - 2] != '#':
            print('No')
            exit()

    for h in range(H):
        if s[h][0] == '#':
            if s[h - 1][0] != '#' and \
                s[h][1] != '#' and \
                    s[h + 1][0] != '#':
                print('No')
                exit()
        if s[h][W - 1] == '#':
            if s[h - 1][W - 1] != '#' and \
                s[h][W - 2] != '#' and \
                    s[h + 1][W - 1] != '#':
                print('No')
                exit()

    for w in range(W):
        if s[0][w] == '#':
            if s[0][w - 1] != '#' and \
                s[1][w] != '#' and \
                    s[0][w + 1] != '#':
                print('No')
                exit()
        if s[H - 1][w] == '#':
            if s[H - 1][w - 1] != '#' and \
                s[H - 2][w] != '#' and \
                    s[H - 1][w + 1] != '#':
                print('No')
                exit()

    for h in range(1, H - 1):
        for w in range(1, W - 1):
            if s[h][w] == '#':
                if s[h - 1][w] != '#' and \
                    s[h + 1][w] != '#' and \
                    s[h][w - 1] != '#' and \
                        s[h][w + 1] != '#':
                    print('No')
                    exit()
    print('Yes')


main()
