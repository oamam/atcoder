N = int(input())
ans = 0


def fn(x):
    global ans
    if int(x) > N:
        return
    if all(x.count(i) for i in '753'):
        ans += 1
    for i in '753':
        fn(x + i)


fn('0')
print(ans)
