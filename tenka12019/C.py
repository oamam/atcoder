def main():
    _ = int(input())
    S = input()
    aw = S.count('.')
    ab = S.count('#')
    w = S.count('.')
    b = 0
    ans = float('INF')
    for s in S:
        if s == '.':
            w -= 1
        if s == '#':
            b += 1
        ans = min(aw, ab, w + b, ans)
    print(ans)


main()
