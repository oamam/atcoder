def main():
    A, B, K = map(int, input().split())
    i = 0
    v = []
    while min(A, B) > i:
        i += 1
        if A % i == 0 and B % i == 0:
            v.append(i)
    print(v[-K])


main()
