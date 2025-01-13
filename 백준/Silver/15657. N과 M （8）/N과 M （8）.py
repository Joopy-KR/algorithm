def solution(n: int, m: int, arr: list, seq: list, before_max:int, max_val:int, now: int):
    if now == m:
        print(" ".join(map(str, seq)))
        return
    for i in range(n):
        if arr[i] < max_val:
            continue
        before_max = max_val
        max_val = arr[i]
        seq[now] = arr[i]
        solution(n, m, arr, seq, before_max, max_val, now + 1)
        max_val = before_max


import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
ARR = list(map(int, input().rstrip().split()))
ARR.sort()
sequence = [0] * M
before_maximum = -1
maximum_value = -1
solution(N, M, ARR, sequence, before_maximum, maximum_value, 0)
