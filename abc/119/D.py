def main():
    A, B, Q = map(int, input().split())
    s = []
    t = []
    ans = []
    for _ in range(A):
        s.append(int(input()))
    for _ in range(B):
        t.append(int(input()))
    for _ in range(Q):
        x = int(input())
        s.append(x)
        s.sort()
        i = s.index(x)
        if i > 0:
            if A > i:
                if s[i] - s[i - 1] > s[i + 1] - s[i]:
                    si = s[i + 1]
                else:
                    si = s[i - 1]
            else:
                si = s[i - 1]
        else:
            si = s[i + 1]
        t.append(x)
        t.sort()
        j = t.index(x)
        if j > 0:
            if B > j:
                if t[j] - t[j - 1] > t[j + 1] - t[j]:
                    tj = t[j + 1]
                else:
                    tj = t[j - 1]
            else:
                tj = t[j - 1]
        else:
            tj = t[j + 1]
        print(si, tj)
        if abs(x - si) > abs(x - tj):
            ans.append(abs(x - tj) + abs(tj - si))
        else:
            ans.append(abs(x - si) + abs(si - tj))
        s.pop(i)
        t.pop(j)
    for a in ans:
        print(a)


main()
