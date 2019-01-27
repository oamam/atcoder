def main():
    S = input()
    if S[0] != 'A':
        print('WA')
        exit()
    if S[2:-1].count('C') != 1:
        print('WA')
        exit()
    s = list(S)
    s[0] = 'a'
    ci = 2 + S[2:-1].index('C')
    s[ci] = 'c'
    if ''.join(s) != S.lower():
        print('WA')
        exit()
    print('AC')


main()
