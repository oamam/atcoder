def main():
    N, T = map(int, input().split())
    m = 1001
    for _ in range(N):
        c, t = map(int, input().split())
        if T >= t and m > c:
            m = c
    if m == 1001:
        print('TLE')
    else:
        print(m)


if __name__ == '__main__':
    main()
