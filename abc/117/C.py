def main():
    N, M = map(int, input().split())
    X = sorted(list(map(int, input().split())))

    if M == 1:
        print(0)
    elif N == 1:
        print(max(X) - min(X))
    else:
        if N > M:
            N = M
        dx = sorted([abs(X[m] - X[m + 1]) for m in range(M - 1)])
        print(sum(dx[:M - N]))


main()
