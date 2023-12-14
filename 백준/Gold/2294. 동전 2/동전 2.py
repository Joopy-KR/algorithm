N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

dp = [10001] * (K + 1)
dp[0] = 0

for coin in coins:
    for total in range(coin, K + 1):
        if dp[total] > 0:
            dp[total] = min(dp[total], dp[total - coin] + 1)

if dp[K] == 10001:
    print(-1)
else:
    print(dp[K])