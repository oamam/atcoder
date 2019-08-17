N = int(input())
T = list(map(int, input().split()))
M = int(input())
ans = []
for _ in range(M):
    p, m = map(int, input().split())
    ans.append(str(sum(T) - T[p - 1] + m))
for a in ans:
    print(a)
