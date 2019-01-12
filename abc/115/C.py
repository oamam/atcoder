def main():
    N, K = list(map(int, input().split()))
    hs = [int(input()) for i in range(N)]
    hs.sort()
    i = 0
    r = 10 ** 9
    while True:
        if i + K > N:
            break
        r = min(r, hs[i + K - 1] - hs[i])
        i += 1
    print(r)


if __name__ == '__main__':
    main()
