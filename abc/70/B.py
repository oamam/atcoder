def main():
    A, B, C, D = map(int, input().split())
    if C > B or A > D:
        print(0)
    else:
        print(min(B, D) - max(A, C))


main()
