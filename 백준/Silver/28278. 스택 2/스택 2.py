import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    order = list(map(int, input().rstrip().split()))

    if len(order) == 1:
        A = order[0]
        if A == 2:
            try:
                print(stack.pop())
            except:
                print(-1)
        elif A == 3:
            print(len(stack))
        elif A == 4:
            if not stack:
                print(1)
            else:
                print(0)
        elif A == 5:
            try:
                print(stack[-1])
            except:
                print(-1)
    else:
        stack.append(order[1])
