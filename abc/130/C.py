def main():
    W, H, x, y = map(int, input().split())
    if (x * 2, y * 2) == (W, H):
        print(W * H / 2, 1, end=' ')
    else:
        print(W * H / 2, 0, end=' ')


main()
