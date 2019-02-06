def main():
    A, B, C, X, Y = map(int, input().split())
    if A + B > C * 2:
        if X >= Y:
            if A > C * 2:
                print(X * C * 2)
            else:
                print((X - Y) * A + Y * C * 2)
        else:
            if B > C * 2:
                print(Y * C * 2)
            else:
                print((Y - X) * B + X * C * 2)
    else:
        print(X * A + Y * B)


main()
