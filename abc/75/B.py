def main():
    H, W = map(int, input().split())
    M = []
    for _ in range(H):
        M.append(input())
    ans = [[''] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if M[i][j] == '#':
                ans[i][j] = '#'
                continue
            c = 0
            for ii, jj in [
                (i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1),
                (i + 1, j - 1), (i - 1, j + 1), (i - 1, j - 1), (i + 1, j + 1)
            ]:
                if 0 <= ii < H and 0 <= jj < W:
                    if M[ii][jj] == '#':
                        c += 1
            ans[i][j] = str(c)
    for a in ans:
        print(''.join(a))


main()
