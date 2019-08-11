import collections

N = int(input())
A = sorted(list(map(int, input().split())))
C = collections.Counter(A)
k = len(collections.Counter(A).keys())
if k % 2 == 1:
    print(k)
else:
    print(k - 1)
