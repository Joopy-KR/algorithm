import sys
input = sys.stdin.readline
import heapq

heap = []
N = int(input().rstrip())
for _ in range(N):
    order = int(input().rstrip())
    if order == 0:
        if not heap:
            print(0)
        else:
            result = heapq.heappop(heap)
            print(result)
    else:
        heapq.heappush(heap, order)