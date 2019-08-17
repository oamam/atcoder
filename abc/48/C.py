N, x = map(int, input().split())
A = list(map(int, input().split()))

ans = max(0, A[0] - x)
p = min(A[0], x)
for i in range(1, N):
    d = p + A[i] - x
    if d > 0:
        A[i] -= d
        ans += d
    p = A[i]
print(ans)
