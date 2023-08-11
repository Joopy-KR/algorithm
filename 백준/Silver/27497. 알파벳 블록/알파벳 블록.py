import sys

N = int(sys.stdin.readline().rstrip())  # 버튼을 누른 횟수 N
result = [0] * 2000000
stack = [0] * N
top = -1
i = 1000000
j = 999999
for _ in range(N):
    order = list(map(str, sys.stdin.readline().rstrip().split()))
    if order[0] == '1':
        top += 1
        stack[top] = 'b'
        i -= 1
        result[i] = order[1]
    elif order[0] == '2':
        top += 1
        stack[top] = 'f'
        j += 1
        result[j] = order[1]
    elif order[0] == '3':
        if top < 0:
            continue
        else:
            top -= 1
            if stack[top+1] == 'b':
                i += 1
            elif stack[top+1] == 'f':
                j -= 1

real_result = ''.join(result[i:j+1])

if not real_result:
    print(0)
else:
    print(real_result[::-1])