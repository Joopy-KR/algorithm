"""
1 - v1 - v2 - N
1 - v2 - v1 - N
두 가지 경우를 비교해서 더 빠른걸 구하면 됨
"""
import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, E = map(int, input().rstrip().split())

arr = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().rstrip().split())
    arr[a].append([b, c])
    arr[b].append([a, c])

v1, v2 = map(int, input().rstrip().split())


def dijkstra(start, end):
    queue = []
    distance = [INF] * (N + 1)
    heapq.heappush(queue, [0, start])
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in arr[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, [cost, i[0]])

    return distance[end]
"""
1 - v1 - v2 - N
1 - v2 - v1 - N
두 가지 경우를 비교해서 더 빠른걸 구하면 됨
"""
start_to_v1 = dijkstra(1, v1)
v1_to_v2 = dijkstra(v1, v2)
v2_to_end = dijkstra(v2, N)

start_to_v2 = dijkstra(1, v2)
v2_to_v1 = dijkstra(v2, v1)
v1_to_end = dijkstra(v1, N)

first_case = start_to_v1 + v1_to_v2 + v2_to_end
second_case = start_to_v2 + v2_to_v1 + v1_to_end

result = min(first_case, second_case)

if result >= INF:
    print(-1)
else:
    print(result)