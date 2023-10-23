"""
정사각형이란 무엇인가... 대각선으로 내려갔을때 차있어야 정사각형이다...
고로 돌면서 1이 나오면 대각선으로
"""

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
result = 0

for r in range(N):
    for c in range(M):
        # 만약 가장자리라면
        if r == 0 or c == 0:
            dp[r][c] = arr[r][c]
        # 만약 원배열 값이 0 이라면 - 볼 필요도 없음. 정사각형일수가 없으니까
        elif arr[r][c] == 0:
            dp[r][c] = 0
        # 뭔가 뭔가 있다면? 내 왼쪽 위쪽 왼쪽대각선을 봐야함! 젤 작은거보다 +1 한게 최대크기!
        else:
            dp[r][c] = min(dp[r][c-1], dp[r-1][c], dp[r-1][c-1]) + 1
        # 최대값 갱신하기
        result = max(dp[r][c], result)

print(result ** 2)