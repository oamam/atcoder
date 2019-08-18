N, L = map(int, input().split())
ans = []
for _ in range(N):
    ans.append(input())
print(''.join(sorted(ans)))
