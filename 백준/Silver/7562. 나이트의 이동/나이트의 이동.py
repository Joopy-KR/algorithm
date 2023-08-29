"""
1. 각 경우에 대해서 전부 돌다가
2. 최소 횟수를 넘으면 그만 돌면 되는거 아닌가?

1. 다르게 생각하면 굳이 2차원 배열 만들 필요 없이
2. 숫자적으로 해결할 수 있지 않을까?
3. 이미 시작점. 종료점을 알고 있기 때문에...

범위를 좁혀나가면서 돌자.
"""


def bfs(s_r, s_c, e_r, e_c):
    dr = [-2, -1, 1, 2, 2, 1, -1, -2]
    dc = [1, 2, 2, 1, -1, -2, -2, -1]
    min_result = 10000
    visited = [[0] * l for _ in range(l)]
    queue = list()
    queue.append([s_r, s_c])
    visited[s_r][s_c] = 1
    while queue:
        r, c = queue.pop(0)
        # 선 자리에서 델타 탐색
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위 안을 돌면서
            if 0 <= nr < l and 0 <= nc < l:
                # 방문한 적이 없다면
                if visited[nr][nc] == 0:
                    queue.append([nr, nc])
                    visited[nr][nc] = visited[r][c] + 1
    return visited[e_r][e_c] - 1


T = int(input())
for tc in range(1, T + 1):
    l = int(input())  # 체스판 한 변의 길이
    s_r, s_c = map(int, input().split())
    e_r, e_c = map(int, input().split())
    arr = [[0] * l for _ in range(l)]

    print(bfs(s_r, s_c, e_r, e_c))
