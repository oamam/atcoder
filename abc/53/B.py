s = input()
n = len(s)
a = float('INF')
z = 0
for i in range(n):
    if s[i] == 'A':
        a = min(a, i)
    elif s[i] == 'Z':
        z = max(z, i)
print(z + 1 - a)
