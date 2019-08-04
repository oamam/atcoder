def f(a, b):
    return max(len(str(a)), len(str(b)))


def main():
    N = int(input())
    ans = float('INF')
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            ans = min(ans, f(i, N // i))
    print(ans)


main()
