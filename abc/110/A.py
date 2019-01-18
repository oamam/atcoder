def main():
    abc = list(input().split())
    abc.sort(reverse=True)
    print(int(''.join(abc[:2])) + int(abc[2]))


main()
