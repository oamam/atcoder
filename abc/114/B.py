def main():
    T = 753
    S = input()
    m = int(S)
    for i in range(len(S)):
        m = min(m, abs(T - int(S[i:i + 3])))
    print(m)


if __name__ == '__main__':
    main()
