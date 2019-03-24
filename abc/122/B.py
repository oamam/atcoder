def main():
    S = input()
    ans = 0
    c = 0
    for s in S:
        if s not in ['A', 'T', 'G', 'C']:
            ans = max(ans, c)
            c = 0
            continue
        c += 1
    print(max(ans, c))


main()
