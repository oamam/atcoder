def f(blue, red, ans):
    c = 0
    for i, b in enumerate(blue):
        for j, r in enumerate(red):
            if b[0] >= r[0] and b[1] >= r[1]:
                blue.pop(i)
                red.pop(j)
                c = max(c, f(blue, red, ans + 1))
                blue.insert(i, b)
                red.insert(j, r)
    return max(c, ans)


def main():
    N = int(input())
    red = [list(map(int, input().split())) for _ in range(N)]
    blue = [list(map(int, input().split())) for _ in range(N)]
    print(f(blue, red, 0))


main()
