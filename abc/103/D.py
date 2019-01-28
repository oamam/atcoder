def main():
    N, M = map(int, input().split())
    ab = [[int(i) for i in input().split()] for _ in range(M)]
    ab = sorted(ab, key=lambda x: x[1] - x[0])
    d = [ab.pop(0)]
    ans = 1
    for a, b in ab:
        flg = True
        for aa, bb in d:
            if b > aa or bb > a:
                flg = False
                break
        if flg is True:
            ans += 1
    print(ans)


main()
