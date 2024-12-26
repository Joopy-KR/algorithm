import sys; input = sys.stdin.readline
N, M = map(int, input().split())
stack = []
def solution(now):
    if len(stack) == M:
        print(" ".join(map(str, stack))); return
    for i in range(now, N + 1):
        stack.append(i)
        solution(i + 1)
        stack.pop()
solution(1)