a, b, c = map(int, input().split())
print('YNeos'[not (a + b == c or a + c == b or b + c == a)::2])
