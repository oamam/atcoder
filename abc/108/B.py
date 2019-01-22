def main():
    x1, y1, x2, y2 = map(int, input().split())
    xx = abs(y1 - y2)
    yy = abs(x1 - x2)
    if x1 > x2:
        if y1 > y2:
            print(x2 + xx, y2 - yy, x1 + xx, y1 - yy)
        else:
            print(x2 - xx, y2 - yy, x1 - xx, y1 - yy)
    else:
        if y1 > y2:
            print(x2 + xx, y2 + yy, x1 + xx, y1 + yy)
        else:
            print(x2 - xx, y2 + yy, x1 - xx, y1 + yy)


main()
