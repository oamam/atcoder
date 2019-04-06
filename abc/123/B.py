import math


def main():
    ans = 0
    t = []
    for _ in range(5):
        x = input()
        if x[-1] == '0':
            ans += int(x)
        else:
            t.append(int(x))
    if len(t) > 0:
        t.sort(key=lambda x: str(x)[-1])
        for i in range(1, len(t)):
            ans += math.ceil(t[i] / 10) * 10
        ans += t[0]
    print(ans)


main()
