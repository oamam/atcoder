import bisect

N = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0

for i in range(N - 2):
    a = L[i]
    for ii in range(i + 1, N - 1):
        b = L[ii]
        iii = bisect.bisect_left(L, a + b)
        ans += iii - ii - 1
            
print(ans)