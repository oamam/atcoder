def main():
    A, B, C = list(map(int, input().split()))
    print('YNeos'[not(min(A, B) < C < max(A, B))::2])


main()
