import heapq
import sys
input = sys.stdin.readline

heap = []
N = int(input().rstrip())
for _ in range(N):
    order = int(input().rstrip())
    if order == 0:
        if heap:
            temp = -1 * heapq.heappop(heap)
            print(temp)
        else:
            print(0)
    else:
        temp = -order
        heapq.heappush(heap, temp)