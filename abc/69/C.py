def main():
    _ = int(input())
    A = list(map(int, input().split()))
    b1 = 0
    b2 = 0
    b4 = 0
    for a in A:
        if a % 2 == 0:
            if a % 4 == 0:
                b4 += 1
            else:
                b2 += 1
        else:
            b1 += 1
    if b2 > 0:
        if b4 >= b1:
            print('Yes')
            return
    else:
        if b4 + 1 >= b1:
            print('Yes')
            return
    print('No')


main()
