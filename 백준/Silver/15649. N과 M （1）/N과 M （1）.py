# 재귀의 시작은 종료조건 설정부터
def solution(n, m, seq, vst, now):
    if now == m:
        print(" ".join(map(str, seq)))
        return
    for i in range(1, n + 1):
        if vst[i]:
            continue
        seq[now] = i
        vst[i] = True
        solution(n, m, seq, vst, now + 1)
        vst[i] = False


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sequence = [0] * M
visited = {i:False for i in range(1, N + 1)}
solution(N, M, sequence, visited, 0)
