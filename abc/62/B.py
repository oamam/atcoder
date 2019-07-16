def main():
    H, W = map(int, input().split())
    ans = '#' * (W + 2)
    for _ in range(H):
        ans += '\n#' + input() + '#'
    ans += '\n' + '#' * (W + 2)
    print(ans)


main()
