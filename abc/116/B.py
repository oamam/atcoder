def main():
    s = int(input())
    logs = {s: 1}
    for m in range(2, 1000000):
        if s % 2 == 0:
            s //= 2
        else:
            s = 3 * s + 1
        if s in logs:
            print(m)
            exit()
        logs[s] = m


main()
