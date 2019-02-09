def main():
    K, A, B = map(int, input().split())
    ans = 1
    if A > 1:
        K -= A - 1
        ans += A - 1
    if K % 2 != 0:
        ans += 1
        K -= 1
    if B - A > 1:
        print((B - A) * (K // 2) + ans)
    else:
        print(ans + K)


main()
