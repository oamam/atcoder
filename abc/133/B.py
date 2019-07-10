def main():
    N, D = map(int, input().split())
    X = []
    for _ in range(N):
        X.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            v = 0
            for a, b in zip(X[i], X[j]):
                v += abs((a - b) ** 2)
            if int(v ** 0.5) == v ** 0.5:
                ans += 1
    print(ans)


main()
