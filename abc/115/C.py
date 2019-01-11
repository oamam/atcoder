def main():
    N, K = list(map(int, input().split()))
    hs = [int(input()) for i in range(N)]
    hs.sort()
    i = 0
    r = 10 ** 9
    while True:
        if i + K > N:
            break
        th = hs[i:i + K]
        r = min(r, th[-1] - th[0])
        i += 1
    print(r)


if __name__ == '__main__':
    main()
