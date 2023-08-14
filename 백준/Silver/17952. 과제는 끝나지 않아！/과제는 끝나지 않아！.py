"""
스택을 써야할 것 같다는 생각이 들지 않니?
광산을 캐는 광부의 마음으로!

두가지 경우가 있다.
1로 받은 경우
1-1. 점수와 시간을 담은 정보를 넣어주고, top에 있는 시간을 하나 빼준다.
1-2. 그리고 시간을 -1 빼준다. 만약 시간이 0이라면, pop 해주고 값을 더해준다.

2. 0으로 받은 경우
2-1. 시간을 -1 빼준다. 만약 시간이 0이라면, pop 해주고 값을 더해준다.
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
stack = []
result = 0

for _ in range(N):
    arr = list(map(int, input().rstrip().split()))

    # 1로 받은 경우
    if arr[0] == 1:
        A = arr[1]
        T = arr[2]

        # 1-1. 점수와 시간을 담은 정보를 넣어주고, top에 있는 시간을 하나 빼준다.
        stack.append([A, T])

        # 1-2. 그리고 시간을 -1 빼준다. 만약 시간이 0이라면, pop 해주고 값을 더해준다.
        stack[-1][1] -= 1
        if stack[-1][1] == 0:
            result += stack[-1][0]
            stack.pop()

    # 0으로 받은 경우
    elif arr[0] == 0:
        if stack:
            # 2-1. 시간을 -1 빼준다. 만약 시간이 0이라면, pop 해주고 값을 더해준다.
            stack[-1][1] -= 1
            if stack[-1][1] == 0:
                result += stack[-1][0]
                stack.pop()

print(result)
