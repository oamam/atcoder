def main():
    A, B = map(int, input().split())
    ans = 0
    if A > B:
        ans += A
        ans += max(A - 1, B)
    else:
        ans += B
        ans += max(A, B - 1)
    print(ans)


main()
