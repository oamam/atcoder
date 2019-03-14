def f(i):
    cnt = (i + 1) // 2
    ans = cnt % 2
    if (i % 2 == 0):
        ans ^= i
    return ans


def main():
    A, B = map(int, input().split())
    print(f(A - 1) ^ f(B))


main()
