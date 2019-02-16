def main():
    N = int(input())
    A = list(map(int, input().split()))
    b = min(A)
    for a in A:
        while True:
            if a % b == 0:
                break
            tb = b
            b = a % b
            a = tb
    print(b)


main()
