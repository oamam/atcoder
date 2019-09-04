A, B = map(int, input().split())
B -= A
ans = 1
if B == 0:
    print(ans)
else:
    ans += B // (A - 1)
    if B % (A - 1) > 0:
        ans += 1
    print(ans)
