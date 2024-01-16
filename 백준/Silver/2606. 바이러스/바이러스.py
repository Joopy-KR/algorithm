from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

arr = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in arr:
    i.sort()


def bfs():
    queue = deque()
    visited = [0] * (N + 1)
    queue.append(1)
    visited[1] = 1
    while queue:
        now = queue.popleft()
        for w in range(len(arr[now])):
            if visited[arr[now][w]] == 0:
                queue.append(arr[now][w])
                visited[arr[now][w]] = 1

    return visited

visited = bfs()
print(sum(visited) - 1)