N = list(map(str, input()))

cnt = 0
for n in N:
    if cnt < 10:
        cnt += 1
        print(n, end='')
    else:
        cnt = 1
        print()
        print(n, end='')