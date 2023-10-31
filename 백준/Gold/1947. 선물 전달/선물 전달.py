import sys
N = int(sys.stdin.readline())

dp = [0] * (N+1)

if N == 1:
    print(0)
else:
    dp[2] = 1
    for i in range(3, N+1):
        dp[i] = ((dp[i-1]+dp[i-2]) * (i-1)) % 1000000000

    print(dp[N])