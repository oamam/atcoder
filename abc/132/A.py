def main():
    S = input()
    for s in S:
        if S.count(s) != 2:
            print('No')
            return
    print('Yes')


main()
