def main():
    N, M = map(int, input().split())
    if abs(N - M) > 1:
        print(0)
        return
    ans = 1
    for i in range(1, N + 1):
        ans = ans * i % 1000000007
    for j in range(1, M + 1):
        ans = ans * j % 1000000007
    if N == M:
        ans = ans * 2 % 1000000007
    print(ans)


main()
