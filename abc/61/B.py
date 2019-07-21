def main():
    N, M = map(int, input().split())
    ans = [0] * N
    for _ in range(M):
        a, b = map(int, input().split())
        ans[a - 1] += 1
        ans[b - 1] += 1
    print(*ans, sep='\n')


main()
