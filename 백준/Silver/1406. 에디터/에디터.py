"""
1. 스택을 두개로 나눠서
2. 커서를 기준으로 오른쪽에 추가 제거 해주고
3. 모든 명령이 끝나면 둘이 합치자
"""
from collections import deque
import sys
input = sys.stdin.readline


stack1 = list(map(str, input().rstrip()))
stack2 = deque()
M = int(input().rstrip())
for _ in range(M):
    order = list(map(str, input().rstrip().split()))

    # 커서를 왼쪽으로 한칸 옮김
    if order[0] == 'L':
        # 커서가 문장의 맨 앞이면 무시
        if stack1:
            stack2.appendleft(stack1.pop())

    elif order[0] == 'D':
        if stack2:
            stack1.append(stack2.popleft())

    elif order[0] == 'B':
        if stack1:
            stack1.pop()

    elif order[0] == 'P':
        stack1.append(order[1])


result = ''.join(stack1) + ''.join(stack2)
print(result)