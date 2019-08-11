N = int(input())
p = 1
for i in range(2, N + 1):
    p *= i
ans = 1
for i in range(2, N + 1):
    if p % i != 0:
        continue
    c = 1
    while p % i == 0:
        p //= i
        c += 1
    ans *= c
print(ans % 1000000007)
