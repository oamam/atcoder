def main():
    S = input()
    for j in range(len(S) - 1, 0, -1):
        if len(S[:j]) % 2 == 1:
            continue
        i = len(S[:j]) // 2
        if S[:i] == S[i:j]:
            print(len(S[:j]))
            break


main()
