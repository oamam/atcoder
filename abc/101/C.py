def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    minA = min(A)
    if (N - A.count(minA)) % (K - 1) == 0:
        print((N - A.count(minA)) // (K - 1))
    else:
        print((N - A.count(minA)) // (K - 1) + 1)


main()
