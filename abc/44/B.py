import collections
for c in collections.Counter(input()).values():
    if c % 2 == 1:
        print('No')
        exit()
print('Yes')
