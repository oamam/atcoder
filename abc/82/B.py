def main():
    if sorted(input()) < sorted(input(), reverse=True):
        print('Yes')
    else:
        print('No')


main()
