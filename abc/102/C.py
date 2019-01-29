def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 10 ** 9
    for b in range(N):
        ans = min(ans, sum([abs(a - (b + j + 1)) for j, a in enumerate(A)]))
        ans = min(ans, sum([abs(a - (-b + j + 1)) for j, a in enumerate(A)]))
    print(ans)


main()
