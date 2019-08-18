N = int(input())
pt = 1
pa = 1
for _ in range(N):
    t, a = map(int, input().split())
    if t >= pt and a >= pa:
        pt = t
        pa = a
    else:
        tt = pt // t
        if pt % t != 0:
            tt += 1
        aa = pa // a
        if pa % a != 0:
            aa += 1
        k = max(tt, aa)
        pt = t * k
        pa = a * k
print(pt + pa)
