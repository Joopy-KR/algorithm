import sys
input = sys.stdin.readline

arr1 = [0] + list(map(str, input().rstrip()))
arr2 = [0] + list(map(str, input().rstrip()))

N = len(arr1) - 1
M = len(arr2) - 1

dp = [[0] * (M + 1) for _ in range(N + 1)]

for r in range(1, N + 1):
    for c in range(1, M + 1):
        if arr1[r] == arr2[c]:
            dp[r][c] = dp[r - 1][c - 1] + 1

result = 0
for i in range(1, N + 1):
    for j in range(1, M + 1):
        result = max(result, dp[i][j])


print(result)