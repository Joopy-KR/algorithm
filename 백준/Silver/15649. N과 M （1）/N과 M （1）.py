import sys
input = sys.stdin.readline


def solution(depth, N, M, arr):
    if depth > M:
        if len(arr) != len(set(arr)):
            return
        print(" ".join(map(str, arr)))
        return
    for i in range(N):
        arr[depth - 1] += 1
        solution(depth + 1, N, M, arr)
    arr[depth - 1] = 0


N, M = map(int, input().rstrip().split())
arr = [0] * M
solution(1, N, M, arr)
