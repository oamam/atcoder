def main():
    s = input()
    t = input()
    ls = len(s)
    lt = len(t)
    dp = [[0] * (lt + 1) for _ in range(ls + 1)]
    for i in range(ls):
        for j in range(lt):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    print(dp)
    ans = ''
    while ls > 0 and lt > 0:
        if s[ls - 1] == t[lt - 1]:
            ls -= 1
            lt -= 1
            ans += s[ls]
            continue
        if dp[ls - 1][lt] > dp[ls][lt - 1]:
            ls -= 1
        else:
            lt -= 1
    print(ans[::-1])


main()
