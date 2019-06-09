import bisect


def main():
    N = int(input())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    C = sorted(list(map(int, input().split())))

    ans = 0
    for b in B:
        ans += bisect.bisect_left(A, b) * (N - bisect.bisect_right(C, b))
    print(ans)


main()
