N = int(input())
B = list(map(int, input().split()))
print(B[0] + sum([min(i, j) for i, j in zip(B, B[1:])]) + B[-1])
