import sys
from collections import deque
input = sys.stdin.readline

def dfs(s, arr):
    stack = []
    visited = []
    stack.append(s)
    now = s
    print(now, end=" ")
    while True:
        visited.append(now)
        for next in arr[now]:
            if next not in visited:
                stack.append(now)
                now = next
                print(next, end=" ")
                break
        else:
            if stack:
                now = stack.pop()
            else:
                break


def bfs(s, arr):
    queue = deque()
    visited = []
    queue.append(s)
    visited.append(s)
    while queue:
        now = queue.popleft()
        print(now, end=" ")
        for next in arr[now]:
            if next in visited:
                continue
            queue.append(next)
            visited.append(next)


N, M, V = map(int, input().split())
arr = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    if b not in arr[a]:
        arr[a].append(b)
        arr[b].append(a)

for i in arr:
    i.sort()

dfs(V, arr)
print()
bfs(V, arr)
