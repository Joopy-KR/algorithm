import sys
input = sys.stdin.readline

from collections import deque

N, Q = map(int, input().rstrip().split())

arr = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    p, q, r = map(int, input().rstrip().split())
    arr[p].append((q, r))
    arr[q].append((p, r))

def solve(k, v):
    result = 0
    # k: 추천 값, v: 동영상 번호(시작점)
    # 각 영상으로 가는 최단거리 구해놓고, K보다 작은건 전부다 보여줘야함
    # 즉, 최단거리를 visited에 저장하면서 가자
    queue = deque()
    visited = [0] * (N + 1)
    queue.append(v)
    visited[v] = 1000000001
    while queue:
        now = queue.popleft()
        for w in range(len(arr[now])):
            # 연결되어 있고 방문한 적이 없다면
            if arr[now][w][1] >= k and visited[arr[now][w][0]] == 0:
                queue.append(arr[now][w][0])
                visited[arr[now][w][0]] = min(visited[now], arr[now][w][1])
                result += 1

    return result


for _ in range(Q):
    k, v = map(int, input().split())
    print(solve(k, v))

