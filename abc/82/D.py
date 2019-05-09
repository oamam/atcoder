s = input()
gx, gy = map(int, input().split())


def dfs(x, y, si, f):
    if len(s) == si:
        if (x, y) == (gx, gy):
            return True
        return False
    ans = False
    if s[si] == 'T':
        return dfs(x, y, si + 1, not f)
    if f:
        for xx, yy in [(x + 1, y), (x - 1, y)]:
            ans = ans or dfs(xx, yy, si + 1, f)
    else:
        for xx, yy in [(x, y + 1), (x, y - 1)]:
            ans = ans or dfs(xx, yy, si + 1, f)
    return ans


def main():
    if dfs(0, 0, 0, True):
        print('Yes')
    else:
        print('No')


main()
