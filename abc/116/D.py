N, K = map(int, input().split())
td = [list(map(int, input().split()))
      for _ in range(N)]
td.sort(key=lambda x: -x[1])
q = []
v = set()
sd = 0
for t, d in td[:K]:
    sd += d
    if t in v:
        q.append(d)
    v.add(t)
ans = len(v) ** 2 + sd
for t, d in td[K:]:
    if 0 >= len(q):
        break
    if t in v:
        continue
    v.add(t)
    md = q.pop()
    sd = sd - md + d
    tans = len(v) ** 2 + sd
    ans = max(ans, tans)
print(ans)
