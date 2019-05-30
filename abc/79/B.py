def main():
    N = int(input())
    la = 2
    lb = 1
    for _ in range(N):
        lc = la + lb
        la = lb
        lb = lc
    print(la)


main()
