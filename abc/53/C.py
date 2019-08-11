x = int(input())
if 1 <= x % 11 <= 6:
    print(x // 11 * 2 + 1)
elif 7 <= x % 11 <= 10:
    print(x // 11 * 2 + 2)
else:
    print(x // 11 * 2)
