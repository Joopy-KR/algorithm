from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque([])

for _ in range(N):
    order = list(map(str, input().rstrip().split()))
    if len(order) == 1:
        o = order[0]
        if o == 'pop':
            if q:
                print(q.popleft())
            else:
                print(-1)
        elif o == 'size':
            print(len(q))
        elif o == 'empty':
            if not q:
                print(1)
            else:
                print(0)
        elif o == 'front':
            if not q:
                print(-1)
            else:
                print(q[0])
        elif o == 'back':
            if not q:
                print(-1)
            else:
                print(q[-1])
    else:
        q.append(order[1])