def solution(n, m, seq, before_num, num, now):
    if now == m:
        print(" ".join(map(str, seq)))
        return
    for i in range(1, n + 1):
        if i < num:
            continue
        before_num = num
        num = i
        seq[now] = i
        solution(n, m, seq, before_num, num, now + 1)
        num = before_num


import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
sequence = [0] * M
before_highest_num = 1
highest_num = -1
solution(N, M, sequence, before_highest_num, highest_num, 0)
