from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
queue = deque()
visited = [0] * 3000001
queue.append(N)
visited[N] = 1

while queue:
    now = queue.popleft()
    if now == K:
        break
    # -1로 이동
    if 0 < now:
        if visited[now - 1] == 0:
            queue.append(now - 1)
            visited[now - 1] = visited[now] + 1
    # +1로 이동
    if now < (K * 2):
        if visited[now + 1] == 0:
            queue.append(now + 1)
            visited[now + 1] = visited[now] + 1
    # *2로 이동
    if now <= K:
        if visited[now * 2] == 0:
            queue.append(now * 2)
            visited[now * 2] = visited[now] + 1

print(visited[K] - 1)