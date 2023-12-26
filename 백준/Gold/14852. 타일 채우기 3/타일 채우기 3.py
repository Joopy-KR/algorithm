import sys
input = sys.stdin.readline

N = int(input().rstrip())

dp = [0] * (N + 1)
dp[0] = 1

if N == 1:
    print(2)
elif N == 2:
    print(7)
elif N == 3:
    print(22)
else:
    dp[1] = 2
    dp[2] = 7

    temp = 0
    for i in range(3, N + 1):
        temp += dp[i - 3]
        dp[i] = (dp[i - 1] * 2 + dp[i - 2] * 3 + temp * 2) % 1000000007

    print(dp[N])