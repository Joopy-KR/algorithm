N = int(input())

if N == 1:
    print(3)
else:
    dp = [0] * (N + 1)
    dp[1] = 3
    dp[2] = 7

    for i in range(3, N + 1):
        dp[i] = (2 * dp[i - 1] + dp[i - 2]) % 9901

    print(dp[N])