"""
10    10     ?

      00

      01

1로 시작하면 한가지 경우

0으로 시작하면 두가지 경우 (*2)
"""
N = int(input())
dp = [0] * (N + 1)
start = 3

if N == 1:
    print(1)
elif N == 2:
    print(1)
elif N == 3:
    print(2)
else:
    def solve(n):
        global dp
        dp[1] = 1
        dp[2] = 1
        dp[3] = 2

        if n == N:
            return dp[n]

        n += 1
        dp[n] = (dp[n - 2] * 2) + dp[n - 3]
        solve(n)


    solve(start)
    print(dp[N])