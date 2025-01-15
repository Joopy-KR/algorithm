import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
stack = []
result = 0

stack.append(arr[0])
for i in range(1, N):
    while stack:
        if stack[-1] <= arr[i]:
            stack.pop()
        else:
            break
    stack.append(arr[i])
    result += len(stack) - 1

print(result)
