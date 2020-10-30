import itertools

N, M = map(int, input().split())
pl = itertools.permutations([i for i in range(1, N + 1)])
ab = [list(map(int, input().split())) for _ in range(M)]
ans = 0
for l in pl:
    if l[0] != 1:
        continue
    f = True
    for i in range(N - 1):
        if not ([l[i], l[i + 1]] in ab or [l[i + 1], l[i]] in ab):
            f = False
            break
    if f:
        ans += 1
print(ans)