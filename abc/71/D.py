def main():
    N = int(input())
    S1 = input()
    S2 = input()
    ans = 3
    i = 0
    while N - 1 > i:
        if S1[i] == S2[i]:
            if S1[i + 1] == S2[i + 1]:
                ans *= 2
            i += 1
        else:
            if N > i + 2 and S1[i + 2] != S2[i + 2]:
                ans *= 3
            else:
                ans *= 2
            i += 2
    print(ans % 1000000007)


main()
