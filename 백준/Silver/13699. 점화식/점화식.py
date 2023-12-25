N = int(input())
result = 0

dp = [0] * (N + 1)

if N == 0:
    print(1)
elif N == 1:
    print(1)
elif N == 2:
    print(2)
elif N == 3:
    print(5)
else:
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 5
    for i in range(4, N + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]

    print(dp[N])