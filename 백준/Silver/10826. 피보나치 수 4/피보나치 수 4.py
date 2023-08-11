import sys


def fibo_dp(n):
    f = [0] * (n+1)
    f[0] = 0
    if n > 0:
        f[1] = 1
    if n > 1:
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
    return f[n]


a = int(sys.stdin.readline())
print(fibo_dp(a))