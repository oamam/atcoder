M, D = map(int, input().split())
ans = 0
for m in range(1, M + 1):
    for d in range(22, D + 1):
        d1 = d % 10
        if 2 > d1:
            continue
        d10 = d // 10
        if d1 * d10 == m:
            ans += 1
print(ans)
