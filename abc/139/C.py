N = int(input())
H = list(map(int, input().split()))
ans = 0
c = 0
for i in range(N - 1):
    if H[i] >= H[i + 1]:
        c += 1
    else:
        ans = max(ans, c)
        c = 0
ans = max(ans, c)
print(ans)
