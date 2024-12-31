def solution(n: int, m: int, sub: list, now: int):
    if now == m:
        print(" ".join(map(str, sub)))
        return
    for i in range(1, n + 1):
        sub[now] = i
        solution(n, m, sub, now + 1)


import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
subsequence = [0] * M
solution(N, M, subsequence, 0)
