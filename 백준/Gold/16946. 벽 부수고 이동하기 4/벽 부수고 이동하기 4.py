"""
1. 1위치를 저장한 후
2. 0위치를 저장한 후
3. 0위치에서 bfs 돌면서 값 더해주기
4. 다 돌면 해당 구역을 고유번호로 만들어놓고, {고유번호: 최댓값} 하나 만들어주기
5. 이제 1돌면서 자기 없어졌을때 인접한 고유번호들 더해주고, 그걸 자기 자신으로 만들기
"""
from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
empty_loc = list()  # 0 위치
wall_loc = list()  # 1 위치
registerd_number = 1
registerd_dict = dict()

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

for r in range(N):
    for c in range(M):
        if arr[r][c] == 0:  # 빈 공간이면
            empty_loc.append([r, c])
        else:
            visited[r][c] = 0
            wall_loc.append([r, c])

for zero_loc in empty_loc:
    zero_r, zero_c = zero_loc
    if visited[zero_r][zero_c] == -1:
        queue = deque()
        queue.append([zero_r, zero_c])
        visited[zero_r][zero_c] = registerd_number
        temp_cnt = 1
        while queue:
            now_r, now_c = queue.popleft()
            for i in range(4):
                nr = now_r + dr[i]
                nc = now_c + dc[i]
                if 0 <= nr < N and 0 <= nc < M:
                    if visited[nr][nc] == -1:
                        queue.append([nr, nc])
                        visited[nr][nc] = registerd_number
                        temp_cnt += 1
        registerd_dict[registerd_number] = temp_cnt
        registerd_number += 1

for one_loc in wall_loc:
    one_r, one_c = one_loc
    near_num = set()
    temp_result = 0
    for i in range(4):
        nr = one_r + dr[i]
        nc = one_c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if visited[nr][nc] != 0:
                near_num.add(visited[nr][nc])
    for num in near_num:
        temp_result += registerd_dict[num]
    arr[one_r][one_c] = (temp_result + 1) % 10

for r in range(N):
    for c in range(M):
        print(arr[r][c], end="")
    print()
