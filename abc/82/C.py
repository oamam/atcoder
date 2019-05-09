import collections


def main():
    _ = int(input())
    a = map(int, input().split())
    c = collections.Counter(a)
    ans = 0
    for i, j in c.items():
        if i > j:
            ans += j
        else:
            ans += j - i
    print(ans)


main()
