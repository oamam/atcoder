def main():
    N = int(input())
    T, A = list(map(int, input().split()))
    H = list(map(int, input().split()))
    m = []
    for h in H:
        m.append(abs(A - (T - h * 0.006)))
    print(m.index(min(m)) + 1)


if __name__ == '__main__':
    main()
