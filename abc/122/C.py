def main():
    N, Q = map(int, input().split())
    S = input()
    SL = [0 for _ in range(len(S))]
    for i in range(len(S) - 1):
        if S[i] == 'A' and S[i + 1] == 'C':
            SL[i + 1] = SL[i] + 1
        else:
            SL[i + 1] = SL[i]
    ans = []
    for _ in range(Q):
        l, r = map(int, input().split())
        ans.append(SL[r - 1] - SL[l - 1])
    for a in ans:
        print(a)


main()
