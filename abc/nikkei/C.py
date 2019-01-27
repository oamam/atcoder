def main():
    N = int(input())
    ab = [[int(i) for i in input().split()] for _ in range(N)]
    ab = sorted(ab, key=lambda x: x[0] + x[1], reverse=True)
    ans = 0
    for i in range(N):
        if i % 2 == 0:
            ans += ab[i][0]
        else:
            ans -= ab[i][1]
    print(ans)


main()
