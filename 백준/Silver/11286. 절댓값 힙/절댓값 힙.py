import sys
import heapq

input = sys.stdin.readline

queue = []

N = int(input().rstrip())
for _ in range(N):
    x = int(input().rstrip())

    if x != 0:
        heapq.heappush(queue, (abs(x), x))
    else:
        if queue:
            print(heapq.heappop(queue)[1])
        else:
            print(0)
