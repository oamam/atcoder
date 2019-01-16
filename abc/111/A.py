def main():
    n = input()
    ans = ''
    for s in n:
        if s == '1':
            ans += '9'
        else:
            ans += '1'
    print(ans)


main()
