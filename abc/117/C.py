N, M = map(int, input().split())
X = list(map(int, input().split()))
X.sort()
d = []
if N > M:
    N = M
for i in range(M - 1):
    d.append(abs(X[i + 1] - X[i]))
d.sort()
print(sum(d[:M - N]))
