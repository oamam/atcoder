def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    ans = 1
    j = 0
    for v in L:
        j += v
        if X >= j:
            ans += 1
        else:
            break
    print(ans)


main()
