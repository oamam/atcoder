def main():
    N = int(input())
    M = []
    for _ in range(5):
        M.append(int(input()))
    x = min(M)
    if x > N:
        print(5)
    else:
        if N % x == 0:
            print(N // x - 1 + 5)
        else:
            print(N // x + 5)


main()
