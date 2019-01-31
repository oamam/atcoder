def main():
    N = int(input())
    an = list(map(int, input().split()))
    ans = 0
    for a in an:
        while True:
            if a % 2 != 0:
                break
            a //= 2
            ans += 1
    print(ans)


main()
