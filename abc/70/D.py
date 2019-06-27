import sys
sys.setrecursionlimit(1000001)

N = int(input())
D = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    D[a].append((b, c))
    D[b].append((a, c))
Q, K = map(int, input().split())
DS = [-1] * (N + 2)


def dfs(c, p, d):
    DS[c] = d
    for r in D[c]:
        if r[0] == p:
            continue
        dfs(r[0], c, d + r[1])


def main():
    dfs(K - 1, -1, 0)
    for _ in range(Q):
        x, y = map(int, input().split())
        print(DS[x - 1] + DS[y - 1])


main()
