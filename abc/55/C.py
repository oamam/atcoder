def main():
    N, M = map(int, input().split())
    k = M // 2
    if N - k >= 0:
        ans = k
    else:
        ans = N
        ans += (M - (N * 2)) // 4
    print(ans)


main()
