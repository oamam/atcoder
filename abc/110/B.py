def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    for t in range(X + 1, Y + 1):
        if t > max(x) and min(y) >= t:
            print('No War')
            exit()
    print('War')


main()
