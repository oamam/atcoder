N = int(input())
A = [list(map(int, input().split())) for _ in range(2)]


def bfs(q):
    ans = 0
    while len(q):
        x, y, c = q.pop(0)
        for xx, yy in [(x + 1, y), (x, y + 1)]:
            if (xx, yy) == (N - 1, 1):
                ans = max(ans, c + A[yy][xx])
            if 0 <= xx < N and 0 <= yy < 2:
                q.append((xx, yy, c + A[yy][xx]))
    return ans


def main():
    print(bfs([(0, 0, A[0][0])]))


main()
