def main():
    N = int(input())
    S = input()
    left = 0
    right = S[1:].count('E')
    ans = right
    for n in range(1, N):
        if S[n - 1] == 'W':
            left += 1
        if S[n] == 'E':
            right -= 1
        ans = min(ans, left + right)
    print(ans)


main()
