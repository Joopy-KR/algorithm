import sys
input = sys.stdin.readline


N = int(input().rstrip())
dp = [1] * N
arr = list(map(int, input().rstrip().split()))
max_result = 0


for end in range(1, N):
    for start in range(0, end):
        if arr[end] > arr[start]:
            dp[end] = max(dp[end], dp[start] + 1)

print(max(dp))
