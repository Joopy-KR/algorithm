import sys
input = sys.stdin.readline


N, M = map(int, input().rstrip().split())

arr = [list(map(str, input().rstrip())) for _ in range(N)]


def DFS(start):
    global is_False
    visited = [[0] * M for _ in range(N)]
    # 색깔 외워두기
    standard = arr[start[0]][start[1]]
    cnt = 1
    stack = []
    # 시작한 곳이면서 끝나야 하는 곳 따로 저장해두기
    visited[start[0]][start[1]] = 2
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    while True:
        r, c = start[0], start[1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위 내에 있고
            if 0 <= nr < N and 0 <= nc < M:
                # 색깔이 같고
                if arr[nr][nc] == standard:
                    # 방문한적이 없다면
                    if visited[nr][nc] == 0:
                        stack.append([r, c])
                        start = [nr, nc]
                        # 색칠해주기
                        visited[nr][nc] = 1
                        # 사이클은 4개 이상의 점으로 이루어져있어야 하므로, 개수 세주기
                        cnt += 1
                        break
                    # 만약 시작점으로 되돌아왔다면? 사이클이 발생한 것!!!
                    # 단, 직전에 출발한 경우라면 제외해야됨...! 당연한소리
                    elif visited[nr][nc] == 2:
                        if cnt >= 4:
                            return True
        else:
            if stack:
                start = stack.pop()
                cnt -= 1
            else:
                break
    return False


result = False
# 그래프 순회하면서 DFS 실행하기
for r in range(N):
    if result is True:
        break
    for c in range(M):
        if DFS([r, c]):
            result = True
            break


if result:
    print('Yes')
else:
    print('No')




