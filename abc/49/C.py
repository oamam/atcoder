S = input()
targets = ['eraser', 'erase', 'dreamer', 'dream']

for tg in targets:
    S = S.replace(tg, '')

if len(S) == 0:
    print('YES')
else:
    print('NO')
