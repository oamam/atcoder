def main():
    X = int(input())
    if X == 1:
        print(1)
    else:
        for x in range(X, 0, -1):
            for b in range(2, X):
                p = 2
                while x >= b ** p:
                    if x == b ** p:
                        print(x)
                        exit()
                    p += 1


main()
