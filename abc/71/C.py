def main():
    N = int(input())
    A = sorted(list(map(int, input().split())), reverse=True)
    i = 0
    d = []
    while N - 1 > i:
        if len(d) == 2:
            break
        if A[i] == A[i + 1]:
            d.append(A[i])
            i += 1
        i += 1
    if (len(d) == 2):
        print(d[0] * d[1])
    else:
        print(0)


main()
