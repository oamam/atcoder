def main():
    N = int(input())
    H = list(map(int, input().split()))
    s = 0
    ans = 0
    for h in H:
        if h >= s:
            ans += 1
            s = h
    print(ans)


main()
