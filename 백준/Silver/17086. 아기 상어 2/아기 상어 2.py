"""
" 제일 작은 놈들 중에 제일 큰놈이 정답"
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
where_is_one = []

for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            where_is_one.append([r, c])

d_r = [-1, -1, 0, 1, 1, 1, 0, -1]
d_c = [0, 1, 1, 1, 0, -1, -1, -1]
visited = [[0] * M for _ in range(N)]

def bfs(start_r, start_c):
    global visited
    queue = []
    queue.append([start_r, start_c])
    visited[start_r][start_c] = 1
    while queue:
        row, col = queue.pop(0)
        for i in range(8):
            nr = row + d_r[i]
            nc = col + d_c[i]
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == 0:
                    queue.append([nr, nc])
                    visited[nr][nc] = visited[row][col] + 1


result = [[1000] * M for _ in range(N)]

for j in where_is_one:
    w_r, w_c = j[0], j[1]
    visited = [[0] * M for _ in range(N)]
    bfs(w_r, w_c)
    for r1 in range(N):
        for c1 in range(M):
            if visited[r1][c1] < result[r1][c1]:
                result[r1][c1] = visited[r1][c1]

max_val = 0
for r2 in range(N):
    for c2 in range(M):
        max_val = max(max_val, result[r2][c2])

print(max_val - 1)