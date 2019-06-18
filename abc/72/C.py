def main():
    _ = int(input())
    A = list(map(int, input().split()))
    C = [0] * (10 ** 5)
    for a in A:
        C[a] += 1
    ans = 0
    for i in range(1, len(C) - 1):
        ans = max(ans, C[i - 1] + C[i] + C[i + 1])
    print(ans)


main()
