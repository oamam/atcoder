def main():
    W, a, b = map(int, input().split())
    m = max(a, b) - min(a, b) - W
    if m > 0:
        print(m)
    else:
        print(0)


main()
