from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
queue = deque()
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            queue.append([r, c])
            visited[r][c] = 0

while queue:
    now = queue.popleft()
    now_r = now[0]
    now_c = now[1]
    for i in range(4):
        nr = now_r + dr[i]
        nc = now_c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] != -1:
                if visited[nr][nc] == -1 or visited[nr][nc] > visited[now_r][now_c] + 1:
                    queue.append([nr, nc])
                    visited[nr][nc] = visited[now_r][now_c] + 1

max_time = 0
is_cant_all = False
for r in range(N):
    for c in range(M):
        if arr[r][c] != -1 and visited[r][c] == -1:
            print(-1)
            is_cant_all = True
            break
        max_time = max(max_time, visited[r][c])
    if is_cant_all:
        break
else:
    print(max_time)
