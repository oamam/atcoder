def main():
    A, B, C = map(int, input().split())
    for i in range(A):
        if (B * i + C) % A == 0:
            print('YES')
            exit()
    print('NO')


main()
