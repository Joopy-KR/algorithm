dp = [[0] * 1001 for _ in range(1001)]

dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 2
dp[3][3] = 1

for i in range(4, 1001):
    for j in range(1, i + 1):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 2][j - 1] + dp[i - 3][j - 1]) % 1000000009

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(dp[N][M])
