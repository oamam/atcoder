def main():
    a, b, c, d = map(int, input().split())
    if (d >= abs(a - b) and d >= abs(b - c)) or d >= abs(a - c):
        print('Yes')
    else:
        print('No')


main()
