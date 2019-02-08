def main():
    S = input()
    if S[:3] == 'yah' and S[3:].count(S[3]) == 2:
        print('YES')
    else:
        print('NO')


main()
