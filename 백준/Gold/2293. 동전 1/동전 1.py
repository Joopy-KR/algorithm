import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
coins = [int(input().rstrip()) for _ in range(N)]
dp = [0] * (K + 1)
dp[0] = 1  # 동전을 쓰지 않는 경우 한가지

for coin in coins:
    for i in range(coin, K + 1):
        dp[i] += dp[i - coin]

print(dp[K])
