def main():
    X, Y = map(int, input().split())
    ans = 0
    while Y >= X:
        X *= 2
        ans += 1
    print(ans)


main()
