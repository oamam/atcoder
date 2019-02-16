def main():
    N, M = map(int, input().split())
    c = [0] * M
    for _ in range(N):
        A = list(map(int, input().split()))[1:]
        for a in A:
            c[a - 1] += 1
    print(c.count(N))


main()
