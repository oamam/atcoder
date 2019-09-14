N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = B[A[0] - 1]
for i in range(1, N):
    a = A[i] - 1
    pa = A[i - 1] - 1
    ans += B[a]
    if 0 <= pa < N - 1 and a == pa + 1:
        ans += C[pa]
print(ans)
