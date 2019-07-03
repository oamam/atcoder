def main():
    N = int(input())
    ans = 1
    while N > ans:
        ans *= 2
    if N == ans:
        print(ans)
    else:
        print(ans // 2)


main()
