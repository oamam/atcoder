N = input()


def check(n, ln):
    if ln == 0:
        if int(N) >= int(n) and all(n.count(s) > 0 for s in '357'):
            return 1
        else:
            return 0
    cnt = 0
    for i in '357':
        cnt += check(n + i, ln - 1)
    return cnt


def main():
    cnt = 0
    for l in range(3, len(N) + 1):
        cnt += check('', l)
    print(cnt)


if __name__ == '__main__':
    main()
