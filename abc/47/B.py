W, H, N = map(int, input().split())
lx = 0
rx = W
dy = 0
uy = H
for _ in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        lx = max(lx, x)
    elif a == 2:
        rx = min(rx, x)
    elif a == 3:
        dy = max(dy, y)
    elif a == 4:
        uy = min(uy, y)
if 0 > rx - lx or 0 > uy - dy:
    print(0)
else:
    print((rx - lx) * (uy - dy))
