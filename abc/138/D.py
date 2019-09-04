N, Q = map(int, input().split())
AB = []
for _ in range(N - 1):
    a, b = map(int, input().split())
    AB.append((a, b))
PX = [0] * (N + 1)
for _ in range(Q):
    p, x = map(int, input().split())
    PX[p] += x
ans = [0] * (N + 1)
p = [False] * (N + 1)
for a, b in AB:
    if PX[a] > 0 and p[a] is False:
        ans[a] += PX[a]
        p[a] = True
    ans[b] += ans[a]
    if PX[b] > 0 and p[b] is False:
        ans[b] += PX[b]
        p[b] = True
print(' '.join(map(str, ans[1:])))
