from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))


def bfs():
    queue = deque()
    visited = [-1] * (N + 1)
    queue.append(0)
    visited[0] = 0
    while queue:
        now = queue.popleft()
        jump = arr[now]
        for j in range(1, jump + 1):
            if now + j < N:
                if visited[now + j] == -1:
                    queue.append(now + j)
                    visited[now + j] = visited[now] + 1
                else:
                    if visited[now + j] > visited[now] + 1:
                        visited[now + j] = visited[now] + 1

    if visited[N - 1] == -1:
        return -1
    else:
        return visited[N - 1]


print(bfs())
