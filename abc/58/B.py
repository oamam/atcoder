def main():
    O = input()
    E = input()
    if len(O) - len(E) == 0:
        ans = ''
        for o, e in zip(O, E):
            ans += o + e
    else:
        ans = O[0]
        for o, e in zip(O[1:], E):
            ans += e + o
    print(ans)


main()
