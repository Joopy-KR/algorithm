N, M = map(int, input().split())
def solution(stack, now):
    if len(stack) == M: print(" ".join(map(str, stack))); return
    for i in range(now, N + 1):
        stack.append(i); solution(stack, i + 1); stack.pop()
solution([], 1)