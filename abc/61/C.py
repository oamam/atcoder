def main():
    N, K = map(int, input().split())
    C = [0] * 100001
    for _ in range(N):
        a, b = map(int, input().split())
        C[a] += b
    for i, c in enumerate(C):
        K -= c
        if 0 >= K:
            print(i)
            break


main()
