import sys
input = sys.stdin.readline

dp = [[0] * 16 for _ in range(16)]
while True:
    try:
        black, white = map(int, input().rstrip().split())
        for b in range(15, -1, -1):
            for w in range(15, -1, -1):
                if b != 0:
                    dp[b][w] = max(dp[b][w], dp[b - 1][w] + black)
                if w != 0:
                    dp[b][w] = max(dp[b][w], dp[b][w - 1] + white)
    except:
        print(dp[15][15])
        break