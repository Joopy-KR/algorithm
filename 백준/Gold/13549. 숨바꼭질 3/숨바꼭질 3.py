import heapq
import sys
INF = sys.maxsize

N, K = map(int, input().split())

arr = [[0] * 100001]

distance = [INF] * 1000001

def dijkstra():
    queue = []
    heapq.heappush(queue, [0, N])
    distance[N] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        for i in [(now + 1, 1), (now - 1, 1), (now * 2, 0)]:
            if 0 <= i[0] < 100001 and distance[i[0]] > dist + i[1]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(queue, [distance[i[0]], i[0]])
    return distance[K]


print(dijkstra())
