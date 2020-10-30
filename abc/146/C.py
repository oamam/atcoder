A, B, X = map(int, input().split())
ans = 0

for i in range(9, -1, -1):
    if A * 10**i + B * i > X:
        continue
    ans = min((X - B * (i + 1)) // A, 10**9)
    break

print(ans)