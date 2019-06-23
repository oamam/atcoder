def main():
    N, L = map(int, input().split())
    a = [L + n for n in range(N)]
    if L > 0:
        print(sum(a) - a[0])
    elif abs(L) >= N:
        print(sum(a) - a[-1])
    else:
        print(sum(a))


main()
