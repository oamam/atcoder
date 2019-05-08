def main():
    c = 'abcdefghijklmnopqrstuvwxyz'
    x = sorted(input())
    y = sorted(input(), reverse=True)
    if x == y[:len(x)] and len(y) > len(x):
        print('Yes')
    else:
        if c.index(x[0]) >= c.index(y[0]):
            print('No')
        else:
            print('Yes')


main()
