import heapq
import sys
input = sys.stdin.readline

N = int(input().rstrip())
present = []
for _ in range(N):
    action = list(map(int, input().rstrip().split()))
    if action == [0]:  # 선물
        if present:
            print(-heapq.heappop(present))
        else:
            print(-1)
    else:  # 거점지
        for idx, a in enumerate(action):
            if idx != 0:
                heapq.heappush(present, -int(a))
