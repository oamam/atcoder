def main():
    ans = sum(map(int, input().split()))
    if ans >= 10:
        print('error')
    else:
        print(ans)


main()
