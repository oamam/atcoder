def main():
    N, A, B = map(int, input().split())
    y = A + B - N
    x = min(A, B)
    if 0 > y:
        y = 0
    print(x, y)


main()
