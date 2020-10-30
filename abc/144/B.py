N = int(input())

if 81 >= N:
    for i in range(1, 10):
        if N % i == 0 and 9 >= N // i:
            print('Yes')
            exit()
print('No')