def gcd(a, b):
    while b > 0:
        c = a % b
        a = b
        b = c
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    A, B, C, D = map(int, input().split())
    E = lcm(C, D)
    bc = B // C
    ac = (A - 1) // C
    bd = B // D
    ad = (A - 1) // D
    blcm = B // E
    alcm = (A - 1) // E
    print(B - A + 1 - ((bc - ac) + (bd - ad) - (blcm - alcm)))


main()
