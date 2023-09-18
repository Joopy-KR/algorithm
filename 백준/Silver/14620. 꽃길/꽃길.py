"""
생각을 해봤는데
1. 어차피 점 하나 찍고 범위 바깥에서 완탐 도는거면
2. 점하나 찍고 돌수 있는 곳을 다 큐에 넣어주고
3. 그 디큐해서 돌때마다 마지막으로 심을수 있는 땅 디큐해서 넣어주고
4. 꽃 세개가 심겼다면 최소값 갱신하기
"""
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

d_r1 = [-1, 0, 1, 0]
d_c1 = [0, 1, 0, -1]

# 맨 끝쪽은 돌아봤자 의미가 없음
for r in range(1, N - 1):
    for c in range(1, N - 1):
        temp_sum = 0
        temp_sum += arr[r][c]
        for i in range(4):
            nr = r + d_r1[i]
            nc = c + d_c1[i]
            # 델타 범위 내에 있다면
            if 0 <= nr < N and 0 <= nc < N:
                temp_sum += arr[nr][nc]
            # 범위 밖으로 나가는 경우는 생각할 필요가 없음
            else:
                temp_sum = 1000
                break
            visited[r][c] = temp_sum

min_val = 10000
# 돌면서 점찍기
for r in range(1, N - 1):
    for c in range(1, N - 1):
        queue = deque()
        temp_result = 0
        temp_result += visited[r][c]
        for r1 in range(1, N - 1):
            for c1 in range(1, N - 1):
                # 꽃잎과 겹치지 않는다면
                if [r1, c1] not in [[r, c], [r-1, c], [r-2, c], [r, c+1], [r-1, c+1], [r, c+2], [r+1, c+1], [r+1, c], [r+2, c], [r+1, c-1], [r, c-1], [r-1, c-1], [r, c-2]]:
                    # 두번째 꽃
                    temp_result += visited[r1][c1]
                    # 꽃잎과 겹치지 않는다면
                    for r2 in range(1, N - 1):
                        for c2 in range(1, N - 1):
                            if [r2, c2] not in [[r, c], [r-1, c], [r-2, c], [r, c+1], [r-1, c+1], [r, c+2], [r+1, c+1], [r+1, c], [r+2, c], [r+1, c-1], [r, c-1], [r-1, c-1], [r, c-2], [r1, c1], [r1-1, c1], [r1-2, c1], [r1, c1+1], [r1-1, c1+1], [r1, c1+2], [r1+1, c1+1], [r1+1, c1], [r1+2, c1], [r1+1, c1-1], [r1, c1-1], [r1-1, c1-1], [r1, c1-2]]:
                                temp_result += visited[r2][c2]
                                if temp_result < min_val:
                                    min_val = temp_result
                                temp_result -= visited[r2][c2]
                    temp_result -= visited[r1][c1]

print(min_val)
