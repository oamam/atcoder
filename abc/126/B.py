def main():
    S = input()
    a = int(S[:2])
    b = int(S[2:])
    if 1 <= a <= 12 and 1 <= b <= 12:
        print('AMBIGUOUS')
    elif 1 <= a <= 12 and (b == 0 or b >= 13):
        print('MMYY')
    elif (a == 0 or a >= 13) and 1 <= b <= 12:
        print('YYMM')
    else:
        print('NA')


main()
