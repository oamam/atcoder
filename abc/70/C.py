def gcd(a, b):
    while b > 0:
        c = a % b
        a = b
        b = c
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def main():
    N = int(input())
    T = []
    for _ in range(N):
        T.append(int(input()))
    t = T[0]
    for i in range(1, N):
        t = lcm(max(t, T[i]), min(t, T[i]))
    print(t)


main()
