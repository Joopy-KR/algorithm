from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = []
for _ in range(N + 1):
    arr.append([])

for _ in range(N - 1):
    n1, n2, d = map(int, input().rstrip().split())
    arr[n1].append([n2, d])
    arr[n2].append([n1, d])

# [[], [[2, 2], [4, 3]], [[1, 2]], [[4, 2]], [[3, 2], [1, 3]]]
# BFS로 탐색하면서 거리를 계산해야 한다.

def BFS(start, target):
    result = 0
    queue = deque()
    visited = [0] * (N + 1)
    queue.append(start)
    visited[start] = 1
    while queue:
        now = queue.popleft()
        if now == target:
            result = visited[now]
        for w in arr[now]:
            if visited[w[0]] == 0:
                queue.append(w[0])
                visited[w[0]] = visited[now] + w[1]
    result -= 1
    return result

for _ in range(M):
    s, e = map(int, input().rstrip().split())
    print(BFS(s, e))
