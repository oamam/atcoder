def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A.sort()
    t = A[0]
    ans = 1
    for i in range(1, N):
        t -= A[i]
        if t == 0:
            ans -= 1
        else:
            t = A[i]
            ans += 1
    print(ans)


main()
