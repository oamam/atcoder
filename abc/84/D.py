import math


limit = 100001


def cs(B):
    C = [0 for i in range(limit + 1)]
    for i in range(3, limit + 1, 2):
        if B[i] and B[(i + 1) // 2]:
            C[i] += 1
    for i in range(3, limit + 1):
        C[i] += C[i - 1]
    return C


def eratosthenes():
    B = [True for _ in range(limit + 1)]
    for i in range(2, limit):
        if i >= math.sqrt(limit):
            break
        for ii in range(i ** 2, limit, i):
            B[ii] = False
    return B


def main():
    Q = int(input())
    C = cs(eratosthenes())
    ans = []
    for _ in range(Q):
        l, r = map(int, input().split())
        ans.append(C[r] - C[l - 1])
    for c in ans:
        print(c)


main()
