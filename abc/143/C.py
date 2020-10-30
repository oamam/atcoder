N = int(input())
S = input()

t = S[0]
ans = 1
for i in range(1, N):
    if t == S[i]:
        continue
    t = S[i]
    ans += 1

print(ans)