def main():
    N, M, X = map(int, input().split())
    A = list(map(int, input().split()))
    left = 0
    right = 0
    for a in A:
        if X > a:
            left += 1
        else:
            right += 1
    print(min(left, right))


main()
