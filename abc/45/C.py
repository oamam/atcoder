S = input()
ans = []


def fn(s, arr):
    ans.append(int(s) + sum(map(int, arr)))
    for i in range(1, len(s)):
        fn(s[i:], arr + [s[:i]])


fn(S, [])
print(sum(ans))
