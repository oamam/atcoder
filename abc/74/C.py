def main():
    A, B, C, D, E, F = map(int, input().split())
    xl = []
    yl = []
    for i in range(31):
        for j in range(31):
            x = 100 * A * i + 100 * B * j
            if F >= x and x > 0 and x not in xl:
                xl.append(x)
    for i in range(F):
        for j in range(F):
            y = C * i + D * j
            if F >= y and y > 0 and y not in yl:
                yl.append(y)
    ax = 3001
    ay = 0
    for x in xl:
        for y in yl:
            if F >= x + y and E / (E + 100) >= y / (x + y) and y / (x + y) > ay / (ax + ay):
                ax = x
                ay = y
    if ax == 3001:
        print(100 * A, 0, end=' ')
    else:
        print(ax + ay, ay, end=' ')


main()
