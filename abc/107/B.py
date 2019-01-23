def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    row = [False] * H
    col = [False] * W

    for i in range(H):
        for j in range(W):
            if a[i][j] == '#':
                row[i] = True
                col[j] = True
    for i in range(H):
        if row[i] is True:
            for j in range(W):
                if col[j] is True:
                    print(a[i][j], end='')
            print()


main()
