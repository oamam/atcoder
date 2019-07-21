def main():
    N, D = map(int, input().split())
    ans = N // (D * 2 + 1)
    if N % (D * 2 + 1) > 0:
        ans += 1
    print(ans)


main()
