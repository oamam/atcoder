def main():
    a, b = map(int, input().split())
    print(sum([c for c in range(1, b - a)]) - a)


main()
