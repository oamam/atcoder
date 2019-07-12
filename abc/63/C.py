def main():
    N = int(input())
    S = sorted([int(input()) for _ in range(N)])
    ans = sum(S)
    if ans % 10 != 0:
        print(ans)
    else:
        for s in S:
            if (ans - s) % 10 != 0:
                print(max(ans - s, s))
                return
        print(0)


main()
