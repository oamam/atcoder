def main():
    N = int(input())
    A = sorted(list(map(int, input().split())))
    i = 0
    d = [0, 0]
    while N - 1 > i:
        if A[i] == A[i + 1]:
            d.append(A[i])
            i += 1
        i += 1
    print(d[-1] * d[-2])


main()
