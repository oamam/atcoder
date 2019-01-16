def main():
    N = input()
    for i in range(10):
        n = int(str(i) * len(N))
        if n >= int(N):
            print(n)
            break


main()
