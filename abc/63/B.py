def main():
    S = sorted(input())
    for i in range(len(S) - 1):
        if S[i] == S[i + 1]:
            print('no')
            return
    print('yes')


main()
