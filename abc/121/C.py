def main():
    N, M = map(int, input().split())
    AB = sorted([tuple(map(int, input().split()))
                 for _ in range(N)], key=lambda x: x[0])
    ans = 0
    for A, B in AB:
        ans += min(M, B) * A
        M -= B
        if 0 >= M:
            break
    print(ans)


main()
