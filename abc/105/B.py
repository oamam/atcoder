def main():
    N = int(input())
    flg = False
    for n in range(N // 7 + 1):
        if (N - 7 * n) % 4 == 0:
            flg = True
            break
    if flg is True:
        print('Yes')
    else:
        print('No')


main()
