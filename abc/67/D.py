N = int(input())
T = [[] for _ in range(N)]


def dfs(k):
    q = [k]
    d = [-1] * N
    d[k] = 0
    while len(q) > 0:
        v = q.pop()
        for i in T[v]:
            if d[i] == -1:
                d[i] = d[v] + 1
                q.append(i)
    return d


def main():
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        T[a].append(b)
        T[b].append(a)
    c = dfs(0)
    d = dfs(N - 1)
    ac = 0
    for x, y in zip(c, d):
        if y >= x:
            ac += 1
    if ac > N // 2:
        print('Fennec')
    else:
        print('Snuke')


main()
