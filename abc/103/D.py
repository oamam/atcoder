def main():
    N, M = map(int, input().split())
    ab = [[int(i) for i in input().split()] for _ in range(M)]
    ab = sorted(ab, key=lambda x: x[1])
    last = ab[0][1] - 1
    ans = 1
    for a, b in ab[1:]:
        if last >= a:
            continue
        ans += 1
        last = b - 1
    print(ans)


main()
