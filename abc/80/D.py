def main():
    N, C = map(int, input().split())
    stc = [[0] * (10 ** 5) for _ in range(C)]
    for _ in range(N):
        s, t, c = map(int, input().split())
        stc[c - 1][s - 1:t] = [1] * (t - s + 1)
    print(max(map(sum, zip(*stc))))


main()
