def main():
    _ = int(input())
    K = int(input())
    ans = 0
    for x in list(map(int, input().split())):
        ans += min(x, K - x) * 2
    print(ans)


main()
