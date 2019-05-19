def main():
    N, K = map(int, input().split())
    ans = 0
    for n in range(1, N + 1):
        s = n
        c = 1
        while K > s:
            s *= 2
            c /= 2
        ans += (1 / N) * c
    print(ans)


main()
