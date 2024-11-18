import sys
input = sys.stdin.readline


def solution(depth, N, M, arr):
    global visited

    if depth > M:
        print(" ".join(map(str, arr)))
        return
    for i in range(1, N + 1):
        arr[depth - 1] += 1
        if not visited[i]:
            visited[i] = True
            solution(depth + 1, N, M, arr)
            visited[i] = False
    arr[depth - 1] = 0


N, M = map(int, input().rstrip().split())
arr = [0] * M
visited = [False] * (N + 1)
solution(1, N, M, arr)
