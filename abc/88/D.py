H, W = map(int, input().split())
S = [input() for _ in range(H)]


def bfs():
    q = [(0, 0, 1)]
    m = [[0 for _ in range(W)] for _ in range(H)]
    while len(q) > 0:
        x, y, c = q.pop(0)
        for xx, yy in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            if (H, W) == (yy + 1, xx + 1):
                return c + 1
            if 0 <= yy < H and 0 <= xx < W and S[yy][xx] == '.' and \
                    m[yy][xx] == 0:
                q.append((xx, yy, c + 1))
                m[yy][xx] = 1
    return -1


def main():
    dc = 0
    for i in range(H):
        dc += S[i].count('.')
    c = bfs()
    if c == -1:
        print(-1)
    else:
        print(dc - c)


main()
