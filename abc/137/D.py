import heapq

N, M = map(int, input().split())
B = [[] * M for _ in range(M)]
for i in range(N):
    a, b = map(int, input().split())
    if a > M:
        continue
    B[M - a].append(b)
ans = 0
h = []
for i in range(M - 1, -1, -1):
    for b in B[i]:
        heapq.heappush(h, b * -1)
    if len(h) > 0:
        ans += heapq.heappop(h) * -1
print(ans)
