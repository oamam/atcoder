def main():
    n = int(input())
    A = input().split()
    if n % 2 == 0:
        print(' '.join(A[1::2][::-1] + A[0::2]))
    else:
        print(' '.join(A[0::2][::-1] + A[1::2]))


main()
