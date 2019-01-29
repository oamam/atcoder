def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [a - i for i, a in enumerate(A)]
    B.sort()
    ans = 0
    for i in range(N):
        ans += abs(A[i] - (B[N // 2] + i))
    print(ans)


main()
