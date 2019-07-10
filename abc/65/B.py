def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    i = 1
    c = 0
    v = [0] * (N + 1)
    while v[i] == 0:
        if A[i - 1] == 2:
            print(c + 1)
            return
        v[i] = 1
        i = A[i - 1]
        c += 1
    print(-1)


main()
