def main():
    A, B, C = input().split()
    print('YNEOS'[A[-1] != B[0] or B[-1] != C[0]::2])


main()
