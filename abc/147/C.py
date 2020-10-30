N = int(input())
t = []
for _ in range(N):
    A = int(input())
    tt = []
    for _ in range(A):
        tt.append(list(map(int, input().split())))
    t.append(tt)
ans = 0
for b in range(1 << N):
    f = True
    c = 0
    for i, tt in enumerate(t):
        if b >> i & 1:
            c += 1
            for x, y in tt:
                if b >> (x - 1) & 1 != y:
                    f = False
                    break
    if f:
        ans = max(ans, c)

print(ans)
