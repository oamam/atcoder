ABC = list(map(int, input().split()))
print('YNEOS'[not (ABC.count(5) == 2 and ABC.count(7) == 1)::2])
