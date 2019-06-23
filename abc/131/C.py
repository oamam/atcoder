import fractions


def main():
    A, B, C, D = map(int, input().split())
    lcm = (C * D) // fractions.gcd(C, D)
    bc = B // C
    ac = A // C
    if A % C == 0:
        ac -= 1
    bd = B // D
    ad = A // D
    if A % D == 0:
        ad -= 1
    blcm = B // lcm
    alcm = A // lcm
    if A % lcm == 0:
        alcm -= 1
    print(B - A + 1 - ((bc - ac) + (bd - ad) - (blcm - alcm)))


main()
