S = input()
ans = 0
for i in range(len(S) - 1):
    ss = S[i] + S[i + 1]
    if ss == 'WB' or ss == 'BW':
        ans += 1
print(ans)
