P = 10**9 + 7
W, H = map(int, input().split())
fact = [0] * (W + H)
fact[0], fact[1] = 1, 1
for i in range(2, W + H):
    fact[i] = (fact[i - 1] * i) % P
print((fact[W + H - 2] * pow(fact[W - 1], P - 2, P) * pow(fact[H - 1], P - 2, P)) % P)
