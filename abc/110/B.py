def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    f = True
    for t in range(X + 1, Y + 1):
        x.append(t)
        y.append(t)
        if max(x) != t or min(y) != t:
            print(x, y)
            f = False
            break
        x.pop(-1)
        y.pop(-1)
    if f is True:
        print('No War')
    else:
        print('War')


main()
