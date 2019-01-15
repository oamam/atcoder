def main():
    N, M = map(int, input().split())
    if N == 1:
        print(M)
    else:
        ans = 0
        for i in range(1, int(M ** 0.5)):
            if M % i != 0:
                continue
            if M >= i * N:
                ans = max(i, ans)
            if M >= M // i * N:
                ans = max(M // i, ans)

        print(ans)


if __name__ == '__main__':
    main()
