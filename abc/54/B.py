def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(N)]
    B = [input() for _ in range(M)]
    for i in range(N):
        for j in range(N):
            f = True
            for k in range(M):
                for l in range(M):
                    if i + k >= N or j + l >= N:
                        f = False
                        break
                    if A[i + k][j + l] != B[k][l]:
                        f = False
                        break
                if f is False:
                    break
            if f is True:
                print('Yes')
                exit()
    print('No')


main()
