"""
1. O(N)으로 배열을 돌면서
2. 빈 공간이 나온다면 BFS를 시작한다
3. 지나간다면 배열을 # 으로 바꿔버리고
4. 델타 탐색을 돌면서 BFS에 추가
5. K면 k_cnt += 1, v면 v_cnt += 1
6. BFS가 종료되면 K_result, v_result 업데이트
7. 이렇게 배열을 전부 돈다
"""
from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().rstrip().split())
arr = [list(map(str, input().rstrip())) for _ in range(R)]

k_result = 0
v_result = 0

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(start):
    global arr
    k_cnt = 0
    v_cnt = 0
    queue = deque()
    queue.append(start)
    if arr[start[0]][start[1]] == "k":
        k_cnt += 1
    elif arr[start[0]][start[1]] == "v":
        v_cnt += 1
    arr[start[0]][start[1]] = "#"
    while queue:
        now_r, now_c = queue.popleft()
        for i in range(4):
            nr = now_r + dr[i]
            nc = now_c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if arr[nr][nc] != "#":
                    queue.append([nr, nc])
                    if arr[nr][nc] == "k":
                        k_cnt += 1
                    elif arr[nr][nc] == "v":
                        v_cnt += 1

                    arr[nr][nc] = "#"

    if k_cnt > v_cnt:
        return [k_cnt, 0]
    else:
        return [0, v_cnt]


for r in range(R):
    for c in range(C):
        if arr[r][c] != "#":
            result = bfs([r, c])
            k_result += result[0]
            v_result += result[1]

print(k_result, v_result)
