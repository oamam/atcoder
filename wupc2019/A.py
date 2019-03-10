def main():
    s = input()
    n = len(s)
    mi = -1
    mf = False
    ans = ''
    for i in range(n):
        if s[i] == 'W':
            if mf is False:
                mf = True
                mi = i
            continue
        if s[i] == 'A' and mf is True:
            ans += 'A'
            ans += 'C' * (i - mi)
            mf = False
            mi = -1
            continue
        if mi > -1:
            ans += 'W' * (i - mi)
            mf = False
            mi = -1
        ans += s[i]
    if mi > -1:
        ans += 'W' * (n - mi)
    print(ans)


main()
