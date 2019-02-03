def main():
    N = int(input())
    L = list(map(int, input().split()))
    m = L.pop(L.index(max(L)))
    if sum(L) > m:
        print('Yes')
    else:
        print('No')


main()
