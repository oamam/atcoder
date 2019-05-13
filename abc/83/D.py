def main():
    s = input()
    i = j = len(s) // 2
    if len(s) % 2 == 0:
        j -= 1
    ss = s[j]
    while len(s) > i and j >= 0 and ss == s[i] and ss == s[j]:
        i += 1
        j -= 1
    print(i)


main()
