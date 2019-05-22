N = int(input())
F = []
P = []
for _ in range(N):
    F.append(list(map(int, input().split())))
for _ in range(N):
    P.append(list(map(int, input().split())))
a = [0] * 20


def dfs(pos):
    if pos == 10:
        if a.count(0) == 20:
            return -1000000000
        score = 0
        for f, p in zip(F, P):
            c = 0
            for aa, ff in zip(a, f):
                if aa == ff == 1:
                    c += 1
            score += p[c]
        return score
    a[pos] = 0
    x = dfs(pos + 1)
    a[pos] = 1
    y = dfs(pos + 1)
    return max(x, y)


def main():
    print(dfs(0))


main()
