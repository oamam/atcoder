def main():
    A, B, C, D = map(int, input().split())
    if A + B > C + D:
        print('Left')
    elif C + D > A + B:
        print('Right')
    else:
        print('Balanced')


main()
