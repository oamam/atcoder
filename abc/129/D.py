H, W = map(int, input().split())
S = [input() for _ in range(H)]


def main():
    cnt = [[0] * W for _ in range(H)]
    for h in range(H):
        done = [0] * W
        for w in range(W):
            if S[h][w] == '#' or done[w] == 1:
                continue
            c = 0
            while W > w + c:
                if S[h][w + c] == '#':
                    break
                c += 1
            for k in range(c):
                cnt[h][w + k] += c
                done[w + k] = 1
    for w in range(W):
        done = [0] * H
        for h in range(H):
            if S[h][w] == '#' or done[h] == 1:
                continue
            c = 0
            while H > h + c:
                if S[h + c][w] == '#':
                    break
                c += 1
            for k in range(c):
                cnt[h + k][w] += c
                done[h + k] = 1
    ans = 0
    for r in cnt:
        for c in r:
            ans = max(ans, c - 1)
    print(ans)


main()
