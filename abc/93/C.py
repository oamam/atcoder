def main():
    A, B, C = map(int, input().split())
    k = max(A, B, C)
    while True:
        if (3 * k - (A + B + C)) % 2 != 0:
            k += 1
            continue
        break
    print((3 * k - (A + B + C)) // 2)


main()
