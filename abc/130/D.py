def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    s = 0
    i = 0
    for j in range(N):
        while K > s:
            if i == N:
                break
            s += A[i]
            i += 1
        if K > s:
            break
        ans += N - i + 1
        s -= A[j]
    print(ans)


main()
