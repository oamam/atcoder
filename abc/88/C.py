def main():
    c1 = list(map(int, input().split()))
    c2 = list(map(int, input().split()))
    c3 = list(map(int, input().split()))
    if abs(c1[0] - c1[1]) == abs(c2[0] - c2[1]) == abs(c3[0] - c3[1]) and \
            abs(c1[0] - c1[2]) == abs(c2[0] - c2[2]) == abs(c3[0] - c3[2]):
        print('Yes')
    else:
        print('No')


main()
