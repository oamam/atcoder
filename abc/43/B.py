S = input()
ans = []
for s in S:
    if s == 'B':
        if len(ans) > 0:
            ans.pop(-1)
    else:
        ans.append(s)
print(''.join(ans))
