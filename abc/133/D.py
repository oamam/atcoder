def main():
    N = int(input())
    A = list(map(int, input().split()))
    x = sum(A) - 2 * sum(A[i] for i in range(1, N, 2))
    ans = [str(x)]
    for i in range(N - 1):
        x = 2 * A[i] - x
        ans.append(str(x))
    print(' '.join(ans))


main()
