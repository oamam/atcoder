N = int(input())
ans = 10**12

for i in range(1, 10**6 + 1):
    if N % i == 0:
        ans = min(ans, i + N // i - 2)

print(ans)
