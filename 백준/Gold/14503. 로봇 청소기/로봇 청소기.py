def solution(n, m, arr, start_pos, direction):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    forward = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    backward = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    now = start_pos
    cleand_cnt = 0
    while True:
        now_r, now_c = now
        # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다
        if arr[now_r][now_c] == 0:
            arr[now_r][now_c] = 2
            cleand_cnt += 1
        for i in range(4):
            nr = now_r + dr[i]
            nc = now_c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 0:  # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
                    direction = (direction - 1) % 4  # 반시계 방향으로 90도 회전한다.
                    # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
                    forw_r = now_r + forward[direction][0]
                    forw_c = now_c + forward[direction][1]
                    if arr[forw_r][forw_c] == 0:
                        now = [forw_r, forw_c]
                    break
        else:  # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
            # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            back_r = now_r + backward[direction][0]
            back_c = now_c + backward[direction][1]
            if arr[back_r][back_c] != 1:
                now = [back_r, back_c]
            else:
                print(cleand_cnt)
                return


import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
start_r, start_c, start_direction = map(int, input().rstrip().split())
ARR = [list(map(int, input().rstrip().split())) for _ in range(N)]
solution(N, M, ARR, [start_r, start_c], start_direction)
