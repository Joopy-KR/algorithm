"""
1. 2차원 배열로 (visited 비슷한거) 만들어서
2. 0행이랑 0열에 111111111111111111111 찍어주고
3. 0행이랑 0열이 아니라면, 길가면서 위에꺼랑 아래꺼 더해서 찍어준다.
4. 박스 두개를 끝내면, 그 값을 곱해준다
"""
import sys
input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())

arr = [[0] * M for _ in range(N)]
cnt = 0
center_r = 0
center_c = 0
# 표 만들기
if K != 0:
    for r in range(N):
        for c in range(M):
            cnt += 1
            arr[r][c] = cnt
            # 동그라미 찾으면
            if arr[r][c] == K:
                 center_r = r
                 center_c = c
else:
    center_r = N - 1
    center_c = M - 1

# 1. 2차원 배열로 (visited 비슷한거) 만들어서
visited = [[0] * M for _ in range(N)]

for r in range(N):
    visited[r][0] = 1
for c in range(M):
    visited[0][c] = 1

# 3. 0행이랑 0열이 아니라면, 길가면서 위에꺼랑 아래꺼 더해서 찍어준다.
# 첫번째 박스
for r in range(1, center_r + 1):
    for c in range(1, center_c + 1):
        visited[r][c] = visited[r][c - 1] + visited[r - 1][c]

first_result = visited[center_r][center_c]

# 두번째 박스
for r in range(N):
    visited[r][center_c] = 1
for c in range(M):
    visited[center_r][c] = 1


for r in range(center_r + 1, N):
    for c in range(center_c + 1, M):
        visited[r][c] = visited[r][c - 1] + visited[r - 1][c]

second_result = visited[N-1][M-1]

print(first_result * second_result)