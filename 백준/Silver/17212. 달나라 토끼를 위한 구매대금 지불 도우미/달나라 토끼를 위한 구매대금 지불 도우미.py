import sys

N = int(input())

dp = [j for j in range(N + 1)]

for i in range(2, N + 1):

    # 기본적으로 현재 금액은 전에 있던거보다 1원 더한건데
    dp[i] = dp[i - 1] + 1

    # 2원짜리로 계산하는게 낫냐
    if i >= 2:
        dp[i] = min(dp[i], dp[i - 2] + 1)

    # 5원짜리로 계산하는게 낫냐
    if i >= 5:
        dp[i] = min(dp[i], dp[i - 5] + 1)

    # 7원짜리로 계산하는게 낫냐
    if i >= 7:
        dp[i] = min(dp[i], dp[i - 7] + 1)

# 그래서 결과적으로 얼마짜리로 계산하는게 낫냐
print(dp[N])
