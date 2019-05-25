def main():
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    BC = []
    for _ in range(M):
        B, C = map(int, input().split())
        BC.append((B, C))
    BC = sorted(BC, key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in BC:
        for _ in range(b):
            if i >= len(A) or A[i] >= c:
                break
            A[i] = c
            i += 1
    print(sum(A))


main()
