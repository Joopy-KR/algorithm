# dp의 시작은 점화식부터
# dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
# 첫번째 집에 세가지 다 칠해보고
# 그 다음부터는 전에 칠한거를 제외한 나머지 두 개 중 더 작은걸로 칠해보기

import sys
input = sys.stdin.readline

N = int(input().rstrip())
costs = [list(map(int, input().rstrip().split())) for _ in range(N)]
INF = float('INF')
result = INF

for first_color in range(3):
    dp = [[INF] * 3 for _ in range(N)]
    dp[0][first_color] = costs[0][first_color]
    for i in range(1, N):
        dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])  # 빨강
        dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])  # 초록
        dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])  # 파랑
    for last_color in range(3):
        if first_color != last_color:
            result = min(result, dp[N - 1][last_color])

print(result)