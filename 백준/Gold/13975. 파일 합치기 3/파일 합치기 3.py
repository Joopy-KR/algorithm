import heapq
import sys
input = sys.stdin.readline

T = int(input().rstrip())
for tc in range(1, T + 1):
    K = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    heapq.heapify(arr)
    result = 0

    while len(arr) > 1:
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        heapq.heappush(arr, first + second)
        result += first + second

    print(result)
