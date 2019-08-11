K, X = map(int, input().split())
l = max(-1000000, X - K + 1)
r = min(1000000, X + K)
ans = []
for i in range(l, r):
    ans.append(str(i))
print(' '.join(ans))
