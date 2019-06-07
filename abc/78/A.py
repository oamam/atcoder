def main():
    X, Y = input().split()
    if int(X, 16) > int(Y, 16):
        print('>')
    elif int(X, 16) < int(Y, 16):
        print('<')
    else:
        print('=')


main()
