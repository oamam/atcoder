import fractions

N = int(input())
A = list(map(int, input().split()))
b = 0
for a in A:
    b += fractions.Fraction(1, a)
print(float(fractions.Fraction(1, b)))
