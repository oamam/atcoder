def main():
    N = int(input())
    A = input()
    B = input()
    C = input()
    ans = 0
    for i in range(N):
        if A[i] == B[i] != C[i] or \
            A[i] != B[i] == C[i] or \
                A[i] == C[i] != B[i]:
            ans += 1
        elif A[i] != B[i] != C[i]:
            ans += 2
    print(ans)


main()
