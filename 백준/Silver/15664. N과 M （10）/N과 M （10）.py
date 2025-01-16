def solution(n, m, arr, seq, before_max, max_num, past_seq, vst, now):
    if now == m:
        if seq not in past_seq:
            print(" ".join(map(str, seq)))
            past_seq.append(seq[:])
        return
    for i in range(n):
        if arr[i] < max_num:
            continue
        if vst[i]:
            continue
        before_max = max_num
        max_num = arr[i]
        vst[i] = True
        seq[now] = arr[i]
        solution(n, m, arr, seq, before_max, max_num, past_seq, vst, now + 1)
        max_num = before_max
        vst[i] = False


import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
ARR = list(map(int, input().rstrip().split()))
ARR.sort()
max_number = -1
before_max_number = -1
sequence = [0] * M
past_sequence = list()
visited = [False] * N
solution(N, M, ARR, sequence, before_max_number, max_number, past_sequence, visited, 0)
