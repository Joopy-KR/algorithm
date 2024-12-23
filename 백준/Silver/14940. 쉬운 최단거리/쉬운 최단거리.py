from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
start_r = 0
start_c = 0
is_found = False
for r in range(N):
    for c in range(M):
        if arr[r][c] == 2:
            start_r = r
            start_c = c
            is_found = True
            break
    if is_found:
        break

visited = [[-1] * M for _ in range(N)]
queue = deque()
queue.append([start_r, start_c])
visited[start_r][start_c] = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

while queue:
    now = queue.popleft()
    now_r = now[0]
    now_c = now[1]

    for i in range(4):
        nr = now_r + dr[i]
        nc = now_c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] != 0 and visited[nr][nc] == -1:
                queue.append([nr, nc])
                visited[nr][nc] = visited[now_r][now_c] + 1

for r in range(N):
    for c in range(M):
        if arr[r][c] == 0:
            visited[r][c] = 0

for r in range(N):
    print(*visited[r])