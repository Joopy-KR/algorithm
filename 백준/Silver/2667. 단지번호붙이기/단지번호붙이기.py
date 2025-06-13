from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, num, n, arr):
    queue = deque()
    queue.append(start)
    arr[start[0]][start[1]] = num
    temp_cnt = 1
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:  # 범위 내 존재한다면
                if arr[nr][nc] == 1:
                    arr[nr][nc] = num
                    queue.append([nr, nc])
                    temp_cnt += 1
    return arr, temp_cnt

N = int(input().rstrip())
ARR = [list(map(int, input().rstrip())) for _ in range(N)]
number = 2
total_cnt = 0
answer = []

for r in range(N):
    for c in range(N):
        if ARR[r][c] == 1:
            ARR, result_cnt = bfs(start=[r, c], num=number, n=N, arr=ARR)
            number += 1
            answer.append(result_cnt)
            total_cnt += 1

answer.sort()
print(total_cnt)
for a in answer:
    print(a)
