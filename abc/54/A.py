def main():
    A, B = map(int, input().split())
    if A - B == 0:
        print('Draw')
    elif A == 1:
        print('Alice')
    elif B == 1:
        print('Bob')
    elif A - B > 0:
        print('Alice')
    elif B - A > 0:
        print('Bob')


main()
