from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())
max_sum = 0
arr = []
for i in range(1, N + 1):
    input_num = int(input().rstrip())
    max_sum += input_num
    arr.append([input_num, i])
arr.sort()
queue = deque(arr)
if max_sum + 1 == N:
    is_correct = False
    for i in range((2 * N) - 1):
        if is_correct:  # 틀려야됨 - 숫자 없애기
            out_num = queue.pop()
            print(out_num[1])
            if out_num[0] > 1:
                queue.append([out_num[0] - 1, out_num[1]])
            elif out_num[0] == 1:
                queue.appendleft([out_num[0] - 1, out_num[1]])
            is_correct = False
        else:  # 맞아야됨 - 0 없애기
            print(queue.popleft()[1])
            is_correct = True
else:
    print(-1)
