def main():
    N = int(input())
    ans = 0
    for n in range(1, N + 1, 2):
        c = 0
        for i in range(1, N + 1):
            if c > 8:
                break
            if n % i != 0:
                continue
            c += 1
        if c == 8:
            ans += 1
    print(ans)


main()
