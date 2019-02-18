def main():
    H, W = map(int, input().split())
    a = [[0] * W]
    for _ in range(H):
        ai = list(map(int, input().split()))
        ai.insert(0, 0)
        a.append(ai)
    ans = []
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if a[i][j] % 2 == 0:
                continue
            if W >= j + 1:
                a[i][j] -= 1
                a[i][j + 1] += 1
                ans.append([i, j, i, j + 1])
        if H >= i + 1 and a[i][j] % 2 != 0:
            a[i][j] -= 1
            a[i + 1][j] += 1
            ans.append([i, j, i + 1, j])
    print(len(ans))
    for row in ans:
        print(' '.join(list(map(str, row))))


main()
