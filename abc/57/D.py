def f(N):
    C = [[0] * 51 for _ in range(51)]
    for i in range(N + 1):
        for j in range(i + 1):
            if j == 0 or i == j:
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    return C


def main():
    N, A, B = map(int, input().split())
    V = sorted(list(map(int, input().split())), reverse=True)
    avg = sum(V[:A]) / A
    n = V.count(V[A - 1])
    p = V[:A].count(V[A - 1])
    C = f(N)
    ans = 0
    if p == A:
        for i in range(A, B + 1):
            ans += C[n][i]
    else:
        ans += C[n][p]
    print(avg)
    print(ans)


main()
