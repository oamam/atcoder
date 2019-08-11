S = list(input())
n = len(S)
ans = [0] * n
c = 0
for i in range(n):
    if S[i] == 'R':
        c += 1
    else:
        ans[i] += c // 2
        ans[i - 1] += (c + 1) // 2
        c = 0

S.reverse()
ans.reverse()

c = 0
for i in range(n):
    if S[i] == 'L':
        c += 1
    else:
        ans[i] += c // 2
        ans[i - 1] += (c + 1) // 2
        c = 0

ans.reverse()
print(' '.join(map(str, ans)))
