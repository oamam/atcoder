def main():
    N = int(input())
    a = 0
    m = 0
    mi = 0
    mm = 0
    for i in range(N):
        a = int(input())
        if a > m:
            mm = m
            m = a
            mi = i
        elif a > mm:
            mm = a
    for i in range(N):
        if i == mi:
            print(mm)
        else:
            print(m)


main()
