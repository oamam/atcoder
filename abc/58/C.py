def main():
    n = int(input())
    S = [input() for _ in range(n)]
    e = [0] * 130
    c = [float('inf')] * 130
    for i in range(97, 97 + 26):
        for s in S:
            if chr(i) in s:
                e[i] += 1
                c[i] = min(c[i], s.count(chr(i)))
    ans = ''
    for i in range(97, 97 + 26):
        if e[i] == n:
            ans += chr(i) * c[i]
    print(ans)


main()
