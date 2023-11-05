"""
반드시 지나가야하는 길이 있으므로
그 길을 지나가기 전 + 지나간 후로 더해서
최소값을 구해내면 됨!
"""
import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

T = int(input().rstrip())
for _ in range(1 ,T + 1):
    # 교차로, 도로, 목적지 후보의 개수
    n, m, t = map(int, input().rstrip().split())
    # 출발지, g, h 사이의 도로를 반드시 지나가야함
    s, g, h = map(int, input().rstrip().split())

    arr = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, d = map(int, input().rstrip().split())
        arr[a].append([b, d])
        arr[b].append([a, d])

    possible_arrival = []

    for _ in range(t):
        x = int(input().rstrip())
        possible_arrival.append(x)


    def dijkstra(start, end):
        distance = [INF] * (n + 1)
        queue = []
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

    min_result = INF + 1
    all_possible_result = []

    for p in possible_arrival:
        start_to_end_result = dijkstra(s, p)
        g_first = dijkstra(s, g) + dijkstra(h, p) + dijkstra(g, h)
        h_first = dijkstra(s, h) + dijkstra(g, p) + dijkstra(h, g)

        if start_to_end_result == g_first:
            all_possible_result.append(p)
        elif start_to_end_result == h_first:
            all_possible_result.append(p)

    all_possible_result.sort()

    if len(all_possible_result) > 1:
        all_possible_result = list(map(str, all_possible_result))
        print(' '.join(all_possible_result))
    else:
        print(*all_possible_result)