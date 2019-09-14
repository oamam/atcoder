N, K = map(int, input().split())
A = list(map(int, input().split()))

mbl = len(format(max(A + [K]), 'b'))
cnt = [0] * mbl

for i in range(mbl):
    for a in A:
        if a & (1 << i):
            cnt[i] += 1

x = 0
for i in range(mbl - 1, -1, -1):
    if N // 2 >= cnt[i] and K >= x + (1 << i):
        x += (1 << i)

ans = 0
for a in A:
    ans += (x ^ a)

print(ans)
