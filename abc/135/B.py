def main():
    _ = int(input())
    P = list(map(int, input().split()))
    c = 0
    for i, p in enumerate(P):
        if i + 1 != p:
            c += 1
    print('YNEOS'[c > 2::2])


main()
