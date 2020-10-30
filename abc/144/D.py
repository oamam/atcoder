import math

a, b, x = map(int, input().split())
s = x / a

if (s >= a * b / 2):
    print(math.atan2(2 * (a * b - s) / a, a) / math.pi * 180)
else:
    print(math.atan2(b, 2 * s / b) / math.pi * 180)

