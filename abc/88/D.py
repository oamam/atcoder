H, W = map(int, input().split())
S = [input() for _ in range(H)]
M = [[float('inf') for _ in range(W)] for _ in range(H)]


def dfs(x, y, c):
    cc = float('inf')
    for xx, yy in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
        if (H, W) == (yy + 1, xx + 1):
            return c + 1
        if 0 <= yy < H and 0 <= xx < W and S[yy][xx] == '.' and \
                (M[yy][xx] > c + 1):
            M[yy][xx] = c + 1
            cc = min(cc, dfs(xx, yy, c + 1))
    return cc


def main():
    ans = 0
    for i in range(H):
        ans += S[i].count('.')
    c = dfs(0, 0, 1)
    if c == float('inf'):
        print(-1)
    else:
        print(ans - c)


main()
