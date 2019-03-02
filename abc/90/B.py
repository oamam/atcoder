def main():
    A, B = map(int, input().split())
    c = 0
    for i in range(A, B + 1):
        if str(i)[:2] == str(i)[4] + str(i)[3]:
            c += 1
    print(c)


main()
