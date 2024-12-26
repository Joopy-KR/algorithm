from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
queue = deque()
visited = [[0] * M for _ in range(N)]
queue.append([0, 0])
visited[0][0] = 1


def solution():
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    while queue:
        now_r, now_c = queue.popleft()
        for i in range(4):
            nr = now_r + dr[i]
            nc = now_c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 1 and visited[nr][nc] == 0:
                    queue.append([nr, nc])
                    visited[nr][nc] = visited[now_r][now_c] + 1
                    if nr == N - 1 and nc == M - 1:
                        print(visited[now_r][now_c] + 1)
                        return


solution()