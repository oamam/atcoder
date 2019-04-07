def main():
    X, Y, Z, K = map(int, input().split())
    A = sorted(list(map(int, input().split())), reverse=True)
    B = sorted(list(map(int, input().split())), reverse=True)
    C = sorted(list(map(int, input().split())), reverse=True)
    AB = []
    for a in A:
        for b in B:
            AB.append(a + b)
    AB.sort(reverse=True)
    ABC = []
    for i in range(min(K, len(AB))):
        for c in C:
            ABC.append(AB[i] + c)
    ABC.sort(reverse=True)
    for x in ABC[:K]:
        print(x)


main()
