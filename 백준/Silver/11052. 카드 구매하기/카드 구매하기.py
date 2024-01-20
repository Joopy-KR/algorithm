N = int(input())

arr = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)

# 일단 다음번 카드는 이전 카드에 필요했던 돈 + 1
# 그 다음으로 내가 들고 있는 돈을 그리디하게 넣는다면?
for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + arr[j])

print(dp[N])