def main():
    N = int(input())
    X = list(map(int, input().split()))
    sx = sorted(X)
    left = sx[N // 2 - 1]
    right = sx[N // 2]
    for x in X:
        if right > x:
            print(right)
        else:
            print(left)


main()
