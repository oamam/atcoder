def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    ans = 0
    for n in range(N):
        A = list(map(int, input().split()))
        if sum([A[m] * B[m] for m in range(M)]) + C > 0:
            ans += 1
    print(ans)


main()            
