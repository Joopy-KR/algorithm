import sys
input = sys.stdin.readline

from collections import deque

N, M, T = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def BFS():
    gram_the_legendary_sword = T + 1
    queue = deque()
    visited = [[0] * M for _ in range(N)]
    queue.append([0, 0])
    visited[0][0] = 1
    while queue:
        now = queue.popleft()
        # 도착하면
        if now[0] == N - 1 and now[1] == M - 1:
            # 비교하기
            return min(visited[now[0]][now[1]] - 1, gram_the_legendary_sword)
        # 그람이 있는 곳에 도착했다면
        if arr[now[0]][now[1]] == 2:
            # 어차피 지금부턴 벽 부수면서 갈 수 있으니까 목적지까지의 최소값만 단순 더해주면 됨
            gram_the_legendary_sword = (visited[now[0]][now[1]] - 1) + ((N - 1) - now[0]) + ((M - 1) - now[1])

        # 델타탐색으로 돌기
        for i in range(4):
            nr = now[0] + dr[i]
            nc = now[1] + dc[i]
            # 범위 내에 있고
            if 0 <= nr < N and 0 <= nc < M:
                # 벽이 아니고
                if arr[nr][nc] != 1:
                    # 방문하지 않았다면
                    if visited[nr][nc] == 0:
                        visited[nr][nc] = visited[now[0]][now[1]] + 1
                        queue.append([nr, nc])

    # 끝까지 돌아도 목적지에 도착하지 못했다면
    return gram_the_legendary_sword


result = BFS()
if result > T:
    print('Fail')
else:
    print(result)


"""
애초에 DFS로 풀면 안되는 문제였다.. 만약 겹치는 길이 나오면 어쩔껀데?
각각의 최단거리를 구하고 그람을 거처가는게 빠른지 그냥 가는게 빠른지만 비교하면 되는 문제였다
앞으로는 최단 거리를 구하는 문제가 나오면 딴생각 하지 말고 BFS로 풀 생각 하자

- DFS 쓰는 경우 : 사이클이 발생하는지 확인할 때 (유니온 파인드 공부하자)
- BFS 쓰는 경우 : 최단 거리/경로 계산할 때 사용 (인접 노드를 우선적으로 탐색하므로)

아래는 DFS로 도전했다가 장렬하게 실패한 코드
심지어 그람 먹으면 벽 제한없이 깰 수 있는데 문제 똑바로 안읽고 저걸 또 그람 썼나 안썼나 확인하고 있다 으휴
(가장 고통스러운 순간... 3시간동안 짠 코드를 쓰레기라는걸 깨닫는 순간...)

def DFS(start, end):
    gram_the_legendary_sword = 0
    spend_time = 0
    result_spend_time = 0
    min_time = T + 1
    stack = []
    visited = [[0] * M for _ in range(N)]
    visited[start[0]][start[1]] = 1
    now = start
    # 시작하기 전에 밟고 있는 땅에 그람 있는지 확인하기
    if arr[start[0]][start[1]] == 2:
        gram_the_legendary_sword += 1
    # 델타 탐색으로 돌기
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    while True:
        for i in range(4):
            nr = now[0] + dr[i]
            nc = now[1] + dc[i]
            # 끝났는지 한번 확인해주기
            if nr == end[0] and nc == end[1]:
                spend_time += 1
                min_time = min(min_time, spend_time)
                result_spend_time = spend_time
                spend_time -= 1
            # 범위 내에 있고
            if 0 <= nr < N and 0 <= nc < M:
                # 방문하지 않았고
                if visited[nr][nc] == 0:
                    # 만약 방문하려는 곳이 길이면:
                    if arr[nr][nc] == 0:
                        # 방문하기
                        # 원래 위치 스택에 저장하기
                        stack.append(now)
                        now = [nr, nc]
                        visited[nr][nc] = 1
                        spend_time += 1
                        break
                    # 벽이면
                    elif arr[nr][nc] == 1:
                        # "전설의 명검" 그람이 있는지 확인
                        if gram_the_legendary_sword:
                            gram_the_legendary_sword -= 1
                            stack.append(now)
                            now = [nr, nc]
                            visited[nr][nc] = 1
                            spend_time += 1
                            break
                    # 그람이면
                    elif arr[nr][nc] == 2:
                        gram_the_legendary_sword += 1
                        stack.append(now)
                        now = [nr, nc]
                        visited[nr][nc] = 1
                        spend_time += 1
                        break
        else:
            if stack:
                # 현재 벽에서 돌아간다면, 그람 복구해주기
                if arr[now[0]][now[1]] == 1:
                    gram_the_legendary_sword += 1
                # 만약 현재 위치에서 그람을 먹었었다면, 그람 회수하기
                elif arr[now[0]][now[1]] == 2:
                    gram_the_legendary_sword -= 1
                # 돌아가기
                now = stack.pop()
                # 돌아가므로 시간 빼주기
                spend_time -= 1
            else:
                break
    return [min_time, result_spend_time]


N, M, T = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

first_start = [0, 0]
second_start = [0, 0]

for r in range(N):
    for c in range(M):
        if arr[r][c] == 2:
            second_start = [r, c]

end = [N - 1, M - 1]


first_to_end = DFS(first_start, end)

first_to_second = DFS(first_start, second_start)

second_to_end = DFS(second_start, end)

result = T + 1

if first_to_end[1] <= T and first_to_second[1] + second_to_end[1] <= T:
    result = min(first_to_end[0], first_to_second[0] + second_to_end[0])

elif first_to_end[1] <= T:
    result = first_to_end[0]

elif first_to_second[1] + second_to_end[1] <= T:
    result = first_to_second[0] + second_to_end[0]

print(result)
"""