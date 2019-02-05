def main():
    s = input()
    K = int(input())
    sk = []
    for i in range(len(s)):
        for j in range(1, K + 1):
            ss = s[i:i + j]
            if ss not in sk:
                sk.append(ss)
    print(sorted(sk)[K - 1])


main()
