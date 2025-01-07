def solution(n, m, arr, seq, now):
    if now == m:
        print(" ".join(map(str, seq)))
        return
    for i in range(n):
        seq[now] = arr[i]
        solution(n, m, arr, seq, now + 1)


import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
ARR = list(map(int, input().rstrip().split()))
ARR.sort()
sequence = [0] * M
solution(N, M, ARR, sequence, 0)
