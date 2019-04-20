def main():
    _, S, K = int(input()), input(), int(input())
    ans = ''
    for s in S:
        if s != S[K - 1]:
            ans += '*'
        else:
            ans += s
    print(ans)


main()
