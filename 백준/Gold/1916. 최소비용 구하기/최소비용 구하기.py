import sys
input = sys.stdin.readline
import heapq

n = int(input().rstrip())
m = int(input().rstrip())
# 인접리스트
graph = [[] for i in range(n + 1)]
for _ in range(m):
    f, t, w = map(int, input().rstrip().split())
    graph[f].append([t, w])

INF = int(1e8)
distance = [INF] * (n + 1)

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = dist + cost

            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

start, end = map(int, input().rstrip().split())
dijkstra(start)
print(distance[end])