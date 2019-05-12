def main():
    _ = int(input())
    A = map(int, input().split())
    ans = float('INF')
    for a in A:
        c = 0
        while a % 2 == 0:
            a //= 2
            c += 1
        ans = min(ans, c)
    print(ans)


main()
