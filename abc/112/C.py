def main():
    N = int(input())
    points = []
    for _ in range(N):
        x, y, h = map(int, input().split())
        points.append((x, y, h))

    for xx, yy, hh in points:
        if hh > 0:
            break
    for cx in range(101):
        for cy in range(101):
            f = True
            H = hh + abs(xx - cx) + abs(yy - cy)
            for x, y, h in points:
                if h != max(H - abs(x - cx) - abs(y - cy), 0):
                    f = False
                    break
            if f is True:
                print(cx, cy, H)
                return


if __name__ == '__main__':
    main()
