import math


def main():
    ab = list(map(int, input().split()))
    print(math.ceil(sum(ab) / len(ab)))


main()
