N = list(map(str, input()))

before_N = N.copy()
N.reverse()

if before_N == N:
    print(1)
else:
    print(0)
