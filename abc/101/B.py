def main():
    N = input()
    if int(N) % sum([int(n) for n in N]) == 0:
        print('Yes')
    else:
        print('No')


main()
