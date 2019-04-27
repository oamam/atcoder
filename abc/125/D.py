def main():
    N = int(input())
    A = list(map(int, input().split()))
    c = 0
    for a in A:
        if 0 > a:
            c += 1
    ans = 0
    absA = [abs(a) for a in A]
    if c % 2 == 0:
        ans = sum(absA)
    else:
        ans = sum(absA) - 2 * min(absA)
    print(ans)
    

main()
