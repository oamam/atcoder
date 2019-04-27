def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = 0
    for i in range(len(A) - 2):
        if 0 == A[i] and 0 > A[i + 1] and 0 > A[i + 2]:
            A[i + 1] *= -1
            A[i + 2] *= -1
            continue
        if 0 > A[i]:
            A[i] *= -1
            A[i + 1] *= -1
        B += A[i]
    if 0 >= A[-2]:
        A[-2] *= -1
        A[-1] *= -1
    print(B + A[-1] + A[-2])


main()
