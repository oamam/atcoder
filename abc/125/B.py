def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for v, c in zip(V, C):
        if v - c > 0:
            ans += v - c
    print(ans)


main()
