def main():
    N = int(input())
    ps = [int(input()) for _ in range(N)]
    print(sum(ps) - max(ps) // 2)


if __name__ == '__main__':
    main()
