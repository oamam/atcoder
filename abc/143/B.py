N = int(input())
D = list(map(int, input().split()))
ans = 0

for i in range(N):
    for ii in range(i + 1, N):
        ans += D[i] * D[ii]

print(ans)