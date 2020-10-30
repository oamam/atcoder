import itertools

N = int(input())
pl = itertools.permutations([i for i in range(N)])
xy = [list(map(int, input().split())) for _ in range(N)]
s = 0
c = 0
for l in pl:
    for i in range(N - 1):
        xi, yi = xy[l[i]]
        xj, yj = xy[l[i + 1]]
        s += ((xi - xj)**2 + (yi - yj)**2)**0.5
    c += 1
print(s / c)