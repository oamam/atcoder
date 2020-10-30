N = int(input())
t = 1
for i in range(2, N + 1):
    t *= i
ans = 1
for i in range(2, N + 1):
    if t % i != 0:
        continue
    c = 1
    while t % i == 0:
        t //= i
        c += 1
    ans *= c
print(ans % (10**9 + 7))