def main():
    c = []
    for _ in range(3):
        c.extend(list(map(int, input().split())))
    for i in range(1, 5):
        if c.count(i) == 3:
            print('NO')
            exit()
    print('YES')


main()
