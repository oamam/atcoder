def main():
    N = int(input())
    wn = [input()]
    ans = True
    for i in range(1, N):
        w = input()
        if ans is False:
            continue
        if wn.count(w) > 0:
            ans = False
        if wn[i - 1][-1] != w[0]:
            ans = False
        wn.append(w)

    if ans is False:
        print('No')
    else:
        print('Yes')


main()
