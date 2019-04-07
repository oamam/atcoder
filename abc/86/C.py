def main():
    N = int(input())
    st, sx, sy = 0, 0, 0
    ans = []
    for _ in range(N):
        nt, nx, ny = map(int, input().split())
        if (nx + ny - sx - sy) > (nt - st):
            ans.append(False)
            continue
        if (nx + ny - sx - sy) % 2 != (nt - st) % 2:
            ans.append(False)
            continue
        ans.append(True)
    print('YNeos'[not all(ans)::2])


main()
