def main():
    abc = list(map(int, input().split()))
    K = int(input())
    print(sum(abc) - max(abc) + max(abc) * 2 ** K)


main()
