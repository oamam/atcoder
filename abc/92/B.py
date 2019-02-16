def main():
    N = int(input())
    D, X = map(int, input().split())
    ans = X
    for i in range(N):
        A = int(input())
        for j in range(D):
            if j * A + 1 > D:
                break
            ans += 1
    print(ans)


main()
