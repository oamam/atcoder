def main():
    N = int(input())
    A = []
    B = []
    AB = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
        AB.append((a, b))
    if sum(A) > max(B):
        print('No')
        return
    AB = sorted(AB, key=lambda x: x[1])
    c = 0
    for a, b in AB:
        c += a
        if c > b:
            print('No')
            return
    print('Yes')


main()
