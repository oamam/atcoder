import collections


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    c = collections.Counter(A)
    print(sum(sorted(list(c.values()), reverse=True)[K:]))


main()
