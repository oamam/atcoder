def main():
    _ = int(input())
    S = input()
    a = 0
    b = 0
    for s in S:
        if s == '(':
            b += 1
            continue
        if s == ')' and b == 0:
            a += 1
            continue
        b -= 1
    print('(' * a + S + ')' * b)


main()
