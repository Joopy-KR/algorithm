def solution(n, m, arr, seq, before_max, max_num, now):
    if now == m:
        print(" ".join(map(str, seq)))
        return
    for i in range(n):
        if arr[i] <= max_num:
            continue
        before_max = max_num
        max_num = arr[i]
        seq[now] = arr[i]
        solution(n, m, arr, seq, before_max, max_num, now + 1)
        max_num = before_max


import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
ARR = list(map(int, input().rstrip().split()))
ARR.sort()
sequence = [0] * M
solution(N, M, ARR, sequence, 0, 0, 0)