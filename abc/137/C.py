N = int(input())
c = {}
for _ in range(N):
    s = ''.join(sorted(list(input())))
    if s in c.keys():
        c[s] += 1
    else:
        c[s] = 0
ans = 0
for k in c.values():
    ans += (k * (k + 1)) // 2
print(ans)
