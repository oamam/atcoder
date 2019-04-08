def main():
    N = int(input())
    ans = []
    for _ in range(N):
        ans.append(int(input()))
    print(len(set(ans)))


main()
