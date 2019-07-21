def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N - 1, -1, -1):
        for j in range(i, N, i + 1):
            B[i] += B[j]
        if B[i] % 2 == 1:
            if A[i] == 1:
                B[i] = 0
            else:
                B[i] = 1
        else:
            if A[i] == 1:
                B[i] = 1
            else:
                B[i] = 0
    print(B.count(1))
    for i, c in enumerate(B):
        if c == 1:
            print(i + 1)


main()
