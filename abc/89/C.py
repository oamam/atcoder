import itertools


def main():
    N = int(input())
    d = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
    for _ in range(N):
        S = input()
        if S[0] in d:
            d[S[0]] += 1
    ans = 0
    for a, b, c in list(itertools.combinations(d.keys(), 3)):
        ans += d[a] * d[b] * d[c]
    print(ans)


main()
