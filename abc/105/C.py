def main():
    N = int(input())
    ans = ''
    while N != 0:
        if N % 2 == 0:
            ans = '0' + ans
        else:
            ans = '1' + ans
            N -= 1
        N //= -2
    if ans == '':
        ans = '0'
    print(ans)


main()
