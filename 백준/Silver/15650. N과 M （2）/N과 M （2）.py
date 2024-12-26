def solution(n, m, seq, vst, now, before_min, min_num):
    if now == m:
        print(" ".join(map(str, seq)))
        return
    for i in range(1, n + 1):
        if vst[i]:  # 중복되는 수열 출력하지 않음
            continue
        if min_num >= i:  # 오름차순 수열만 출력함
            continue
        before_min = min_num
        min_num = i
        vst[i] = True
        seq[now] = i
        solution(n, m, seq, vst, now + 1, before_min, min_num)
        min_num = before_min
        vst[i] = False


import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
sequence = [0] * M
visited = [False] * (N + 1)
solution(N, M, sequence, visited, 0, 0, 0)
