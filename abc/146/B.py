N = int(input())
S = input()

ans = ''

for s in S:
    o = ord(s) + N
    if o > 90:
        ans += chr(o - 26)
    else:
        ans += chr(o)

print(ans)
