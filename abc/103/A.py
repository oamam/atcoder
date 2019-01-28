def main():
    A1, A2, A3 = map(int, input().split())
    print(max(A1, A2, A3) - min(A1, A2, A3))


main()
