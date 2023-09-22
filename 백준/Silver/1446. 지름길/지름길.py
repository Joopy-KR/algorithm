import heapq
import sys
input = sys.stdin.readline

N, D = map(int, input().rstrip().split())

pq = []
for _ in range(N):
    # 1. 도착지점이 고속도로의 끝보다 크면 보지도 않는다
    f, t, w = map(int, input().rstrip().split())
    if t > D or f > D:
        continue

    # 지름길이 아니면(그냥 가는거보다 더 오래걸리면) 보지도 않는다
    if t - f < w:
        continue

    heapq.heappush(pq, [f, t, w])

road = [100000000] * (D + 1)
road[0] = 0
start = 1
end = 0
"""
생각을 바꾸자
숫자가 나오면 now까지 1씩 더해주면서 갱신해주고
이걸 토대로 next를 구하는거다
최소값 갱신 해주면서
근데 어디부터..? 바뀐거부터 확인하면 안되나? 그 이전 확인할 필요가 있나?
"""
while pq:
    now, next, dist = heapq.heappop(pq)

    if road[next] < dist:
        continue

    for r in range(1, now + 1):
        road[r] = min(road[r - 1] + 1, road[r])

    # 만약 시작 지점의 최소값이 저장되어 있다면
    if road[now] != 100000000:
        # 그거에 더해서 저장을 해주고
        road[next] = min(road[next], road[now] + dist)
    # 1억으로 저장되어 있다면
    else:
        # 시작 지점 전 제일 가까운 최소값에서부터 1씩 더하면서 저장해준다
        for i in range(now, -1, -1):
            if road[i] != 100000000:
                road[next] = (now - i) + road[i] + dist
                break
        # 만약 처음까지 1억밖에 없으면?
        else:
            road[now] = now
            road[next] = road[now] + dist

    end = next
    for r in range(1, end + 1):
        road[r] = min(road[r - 1] + 1, road[r])

if end != D + 1:
    for r in range(end, D + 1):
        road[r] = min(road[r - 1] + 1, road[r])

print(road[D])