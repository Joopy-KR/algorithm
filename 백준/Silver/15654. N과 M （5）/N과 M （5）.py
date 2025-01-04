def solution(n, m, arr, seq, vst, now):
    if now == m:
        print(" ".join(map(str, seq)))
        return
    for i in range(n):
        if vst[i]:
            continue
        vst[i] = True
        seq[now] = arr[i]
        solution(n, m, arr, seq, vst, now + 1)
        vst[i] = False
        seq[now] = 0


import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
ARR = list(map(int, input().rstrip().split()))
ARR.sort()
sequence = [0] * M
visited = [False] * N
solution(N, M, ARR, sequence, visited, 0)
