"""
1부터 오른쪽 위로 올라가면서 검사하고
바로 다음 이동을 전부 다 채운 다음
그쪽도 오른쪽 위로 올라가면서 전부 검사한다
"""
# 순서 : 1 2 3 4 5 6 7
# 배열 : 1 2 1 3 1 2 1

#   1 2 3 4 5 6 7
# 1 1 0 1 0 0 0 1
# 2   1 0 0 0 1 0
# 3     1 0 1 0 0
# 4       1 0 0 0
# 5         1 0 1
# 6           1 0
# 7             1
import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
dp = [[0] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1

for i in range(N):  # 떨어진 검사
    now_r = i
    now_c = i
    while True:
        now_r -= 1
        now_c += 1
        if 0 <= now_r < N and 0 <= now_c < N:
            if arr[now_r] == arr[now_c]:
                dp[now_r][now_c] = 1
            else:
                break
        else:
            break

for i in range(N - 1):
    if arr[i] == arr[i + 1]:
        dp[i][i + 1] = 1

for i in range(N):  # 붙어있는 검사
    now_r = i
    now_c = i + 1
    if 0 <= now_r < N and 0 <= now_c < N and dp[now_r][now_c] == 0:
        continue
    while True:
        now_r -= 1
        now_c += 1
        if 0 <= now_r < N and 0 <= now_c < N:
            if arr[now_r] == arr[now_c]:
                dp[now_r][now_c] = 1
            else:
                break
        else:
            break

M = int(input().rstrip())
for _ in range(M):
    S, E = map(int, input().rstrip().split())
    print(dp[S - 1][E - 1])

# 디버깅용 코드
# print()
# for r in range(N):
#     for c in range(N):
#         if c < r:
#             print("", end=" ")
#         else:
#             print(dp[r][c], end=" ")
#     print()