def main():
    s = list(input())
    t = list(input())
    n = len(s)
    memo1 = {}
    memo2 = {}

    for i in range(n):
        c1 = s[i]
        c2 = t[i]
        if (c1 in memo1 and memo1[c1] != c2) or \
                (c2 in memo2 and memo2[c2] != c1):
            print('No')
            exit()
        memo1[c1] = c2
        memo2[c2] = c1

    print('Yes')


main()
