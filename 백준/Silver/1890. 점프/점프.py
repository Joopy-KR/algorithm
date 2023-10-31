import sys
input = sys.stdin.readline


N = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for r in range(N):
    for c in range(N):
        if r == N - 1 and c == N - 1:
            print(dp[N-1][N-1])
        move = arr[r][c]
        if r + move < N:
            dp[r + move][c] += dp[r][c]
        if c + move < N:
            dp[r][c + move] += dp[r][c]