def main():
    N = int(input())
    s = [input() for _ in range(N)]
    M = int(input())
    t = [input() for _ in range(M)]
    ans = 0
    for ss in s:
        ans = max(ans, s.count(ss) - t.count(ss))
    print(ans)


main()
