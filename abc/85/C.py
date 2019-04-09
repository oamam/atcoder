def main():
    N, Y = map(int, input().split())

    for i in range(N + 1):
        for ii in range(N - i + 1):
            if i * 10000 + ii * 5000 + (N - i - ii) * 1000 == Y:
                print(i, ii, N - i - ii, end=' ')
                return
    print('-1 -1 -1')


main()
