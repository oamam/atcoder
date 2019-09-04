N, K = map(int, input().split())
A = list(map(int, input().split()))
c = 0
for i in range(N):
    for j in range(i + 1, N):
        if A[i] > A[j]:
            c += 1
cc = 0
for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            cc += 1
ans = c * K
ans += cc * (K - 1) * K // 2
print(ans % 1000000007)
