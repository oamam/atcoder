Sa = input()
Sb = input()
Sc = input()
ai = 0
bi = -1
ci = -1


def fn(s):
    global ai
    global bi
    global ci
    if s == 'a':
        ai += 1
        if len(Sa) == ai:
            print('A')
            exit()
        fn(Sa[ai])
    elif s == 'b':
        bi += 1
        if len(Sb) == bi:
            print('B')
            exit()
        fn(Sb[bi])
    elif s == 'c':
        ci += 1
        if len(Sc) == ci:
            print('C')
            exit()
        fn(Sc[ci])


fn(Sa[0])
