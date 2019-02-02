def main():
    N = int(input())
    S = input()
    ans = 0
    for n in range(N + 1):
        c = 0
        for s in set(S[:n]):
            if S[n:].count(s) > 0:
                c += 1
        ans = max(ans, c)
    print(ans)


main()
