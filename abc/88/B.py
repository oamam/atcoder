def main():
    N = int(input())
    an = sorted(list(map(int, input().split())), reverse=True)
    print(sum(an[i] for i in range(0, N, 2)) -
          sum(an[j] for j in range(1, N, 2)))


main()
