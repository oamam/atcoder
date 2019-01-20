def main():
    N = int(input())
    h = list(map(int, input().split()))
    c = h[0]
    for i in range(N - 1):
        if h[i + 1] > h[i]:
            c += h[i + 1] - h[i]
    print(c)


main()
