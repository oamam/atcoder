from operator import itemgetter


def main():
    N = int(input())
    SP = []
    for n in range(N):
        s, p = input().split()
        SP.append((n + 1, s, int(p)))
    SP = sorted(SP, key=itemgetter(2), reverse=True)
    SP = sorted(SP, key=itemgetter(1))
    for n, s, p in SP:
        print(n)


main()
