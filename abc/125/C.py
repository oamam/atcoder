def main():
    N = int(input())
    A = list(map(int, input().split()))
    L = []
    for i in range(len(A) - 1):
        a = A[i + 1]
        b = A[i]
        while True:
            r = a % b
            if r == 0:
                L.append(b)
                break
            a = b
            b = r
    LL = list(set(L))
    if len(LL) == 1:
        print(LL[0] * 2)
        return
    ans = 0
    for i in LL:
        if len(L) == L.count(i) + 1:
            ans = max(ans, i)
    print(ans)


main()