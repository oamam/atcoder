import fractions

N = int(input())
V = list(map(int, input().split()))
V.sort()
ans = fractions.Fraction(V[0] + V[1], 2)
for i in range(2, N):
    ans = fractions.Fraction((ans + V[i]), 2)
print(float(ans))
