def main():
    X, K = map(int, input().split())
    print((X // 10 ** K + 1) * 10 ** K)


main()
