def main():
    N = int(input())
    c = {3: 'Three', 4: 'Four'}
    print(c[len(set(input().split()))])


main()
