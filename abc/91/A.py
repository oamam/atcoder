def main():
    A, B, C = map(int, input().split())
    print('YNeos'[(C > A + B)::2])


main()
