def main():
    N = int(input())
    red = sorted(
        [list(map(int, input().split())) for _ in range(N)],
        key=lambda x: x[1],
        reverse=True
    )
    blue = sorted(
        [list(map(int, input().split())) for _ in range(N)],
        key=lambda x: x[0]
    )
    ans = 0
    for b in blue:
        for i, r in enumerate(red):
            if b[0] > r[0] and b[1] > r[1]:
                ans += 1
                red.pop(i)
                break
    print(ans)


main()
