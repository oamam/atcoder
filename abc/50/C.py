N = int(input())
A = list(map(int, input().split()))
C = [0] * N
for a in A:
    C[a] += 1
if N % 2 == 1:
    if C[0] != 1:
        print(0)
        exit()
    for i in range(2, N, 2):
        if C[i] != 2:
            print(0)
            exit()
    print(2 ** ((N - 1) // 2) % 1000000007)
else:
    for i in range(1, N, 2):
        if C[i] != 2:
            print(0)
            exit()
    print(2 ** (N // 2) % 1000000007)
