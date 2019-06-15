def main():
    S = list(input())
    T = list(input())
    S.reverse()
    T.reverse()
    SL = list(S)
    f = False
    for i in range(len(S) - len(T) + 1):
        SL = list(S)
        for j in range(len(T)):
            if S[i + j] == '?' or S[i + j] == T[j]:
                SL[i + j] = T[j]
            else:
                break
        else:
            f = True
            break
    if f is False:
        print('UNRESTORABLE')
    else:
        SL.reverse()
        print(''.join(SL).replace('?', 'a'))


main()
