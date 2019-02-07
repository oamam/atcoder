def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 2:
        print(max(a), min(a))
    else:
        ma = max(a)
        sa = sorted([(i, abs(ma // 2 - a[i]))
                     for i in range(n)], key=lambda x: x[1])
        print(ma, a[sa[0][0]])


main()
