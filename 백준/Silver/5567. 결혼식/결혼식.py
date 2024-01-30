from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)


def bfs():
    queue = deque()
    visited = [0] * (N + 1)
    queue.append(1)
    visited[1] = 1
    while queue:
        now = queue.popleft()
        for w in arr[now]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = visited[now] + 1

    result = 0
    for i in range(1, N + 1):
        if 0 < visited[i] <= 3:
            result += 1

    # 자기 자신 빼주기
    result -= 1
    return result


print(bfs())
