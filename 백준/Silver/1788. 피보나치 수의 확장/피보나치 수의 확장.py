import sys
input = sys.stdin.readline

def fibo(N):
    f = [0] * (N + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, N + 1):
        f[i] = (f[i - 1] + f[i - 2]) % 1000000000
    return f[N]

N = int(input().rstrip())
if N == 0:
    print(0)
    print(0)
else:
    if N < 0:
        if N % 2 == 0:
            sign = -1
        else:
            sign = 1
    else:
        sign = 1

    N = abs(N)

    print(sign)
    print(fibo(N))