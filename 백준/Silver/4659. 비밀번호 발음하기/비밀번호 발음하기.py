vowel = ['a', 'e', 'i', 'o', 'u']
while True:
    S = input()
    is_True = None
    v = 0
    nv = 0
    if S == 'end':
        break
    else:
        for i in S:
            if i in vowel:
                is_True = True
                nv = 0
                v += 1
            else:
                v = 0
                nv += 1
            if v == 3 or nv == 3:
                is_True = False
                break
        check = 0
        for j in S:
            if j != 'e' and j != 'o':
                s_check = ord(j)
                if s_check == check:
                    is_True = False
                else:
                    check = s_check


    if is_True:
        print(f'<{S}> is acceptable.')
    else:
        print(f'<{S}> is not acceptable.')