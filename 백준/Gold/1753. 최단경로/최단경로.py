import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

# V: 정점의 개수, E: 간선의 개수
V, E = map(int, input().rstrip().split())
# 시작 정점 번호
K = int(input().rstrip())

# 노드 정보 그래프 만들기
arr = [[] for _ in range(V + 1)]

# 최단 거리 테이블 무한으로 초기화하기
distance = [INF] * (V + 1)

# u: 출발지 v: 도착지 w: 가중치
for _ in range(E):
    u, v, w = map(int, input().split())
    # arr[0] = 노드 번호 / arr[1] = 가중치
    arr[u].append([v, w])


def dijkstra(start):
    queue = []
    # 자기 자신 0 으로 설정하기
    # 힙큐이기 떄문에 거리, 노드번호 순으로 받는다!!!
    heapq.heappush(queue, [0, start])
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        # 이미 방문한 노드라면(테이블에 있는 거리가 더 짧다면) 넘어가기
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 노드들 확인하기
        for i in arr[now]:
            # 가중치 계산하기 (노드로부터의 가중치 + 지금까지의 가중치)
            cost = dist + i[1]
            # 만약 이걸 거쳐가는게 더 싸게 먹힌다면?
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, [cost, i[0]])


# 다익스트라 알고리즘 수행
dijkstra(K)

# 출력하기
for i in range(1, V + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])