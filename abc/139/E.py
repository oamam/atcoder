N = int(input())
A = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]
t = [0] * N
ans = 0
e = [False] * N
v = [True] * N
while any(v):
    v = [False] * N
    for i in range(N):
        if e[i] is True or v[i] is True:
            continue
        j = A[i][t[i]]
        if e[j] is True or v[j] is True:
            continue
        if A[j][t[j]] == i:
            t[i] += 1
            t[j] += 1
            v[i] = True
            v[j] = True
            if t[i] == N - 1:
                e[i] = True
            if t[j] == N - 1:
                e[j] = True
    ans += 1
if not all(e):
    print(-1)
else:
    print(ans - 1)
