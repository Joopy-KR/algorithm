import heapq
import sys
INF = sys.maxsize
input = sys.stdin.readline

tc = 0
while True:
    N = int(input().rstrip())
    tc += 1
    if N == 0:
        break
    else:
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
        distance = [[INF] * (N + 1) for _ in range(N + 1)]
        queue =[]
        heapq.heappush(queue, [arr[0][0], [0, 0]])
        distance[0][0] = arr[0][0]

        while queue:
            dist, now = heapq.heappop(queue)
            now_r = now[0]
            now_c = now[1]

            for i in range(4):
                nr = now_r + dr[i]
                nc = now_c + dc[i]

                if 0 <= nr < N and 0 <= nc < N:
                    # 이미 방문한 노드라면(테이블에 있는 거리가 더 짧다면) 넘어가기
                    if distance[nr][nc] < dist:
                        continue
                    else:
                        cost = dist + arr[nr][nc]

                        if cost < distance[nr][nc]:
                            distance[nr][nc] = cost
                            heapq.heappush(queue, [cost, [nr, nc]])

        print(f'Problem {tc}: {distance[N - 1][N - 1]}')