def main():
    S = input()
    L = []
    LL = []
    i = 0
    for _ in range(len(S)):
        L.append(str(1 ^ i))
        i ^= 1
    i = 0
    for _ in range(len(S)):
        LL.append(str(0 ^ i))
        i ^= 1
    L = ''.join(L)
    LL = ''.join(LL)
    lc = 0
    llc = 0
    for s, l, ll in zip(S, L, LL):
        if s != l:
            lc += 1
        if s != ll:
            llc += 1
    print(min(lc, llc))


main()
