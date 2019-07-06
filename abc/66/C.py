def main():
    n = int(input())
    A = input().split()
    B = [0] * n
    k = n % 2
    l = n // 2
    if k == 0:
        l -= 1
    r = l + 1
    for i in range(n):
        if i % 2 != k:
            B[l] = A[i]
            l -= 1
        else:
            B[r] = A[i]
            r += 1
    print(' '.join(B))


main()
