def main():
    L = [0] * 26
    for s in input():
        L[ord(s) - 97] = 1
    for i, j in enumerate(L):
        if j == 0:
            print(chr(97 + i))
            return
    print('None')


main()
