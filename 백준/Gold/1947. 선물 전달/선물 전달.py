N = int(input())

if N == 1:
    print(0)
else:
    dp = [0] * (N + 1)
    dp[0] = 0
    dp[1] = 0
    dp[2] = 1

    for i in range(3, N + 1):
        dp[i] = ((dp[i-2] + dp[i-1]) * (i - 1)) % 1000000000

    print(dp[N])