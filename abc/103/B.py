def main():
    S = input()
    T = input()

    for _ in range(len(S)):
        S = S[-1] + S[:-1]
        if S == T:
            print('Yes')
            exit()
    print('No')


main()
