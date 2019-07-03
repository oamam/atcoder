def main():
    N, M = map(int, input().split())
    C = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        if a == 1:
            C[b] += 1
        elif b == N:
            C[a] += 1
    if C.count(2) > 0:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')


main()
