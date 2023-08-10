import sys

stack = [] * 1

def push(s):
    stack.append(s)
    return stack

N = int(input())
top = -1

for _ in range(N):
    arr = list(map(str, sys.stdin.readline().split()))
    if arr[0] == 'push':
        top += 1
        push(arr[1])
    elif arr[0] == 'pop':
        if top < 0:
            print(-1)
        else:
            top -= 1
            print(stack.pop())
    elif arr[0] == 'size':
        cnt = 0
        for i in range(0, top+1):
            cnt += 1
        print(cnt)
    elif arr[0] == 'empty':
        if top < 0:
            print(1)
        else:
            print(0)
    elif arr[0] == 'top':
        if top < 0:
            print(-1)
        else:
            print(stack[top])