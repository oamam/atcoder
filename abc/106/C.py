def main():
    S = list(map(int, input()))
    K = int(input())

    for i in S:
        if i == 1:
            K -= 1
            if K == 0:
                print(1)
                exit()
            continue
        j = 1
        while i < 5 * 10 ** 15:
            if i ** j >= K:
                print(i)
                exit()
            j += 1
        K -= i ** j


main()
