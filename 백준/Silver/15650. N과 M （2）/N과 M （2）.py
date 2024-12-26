N, M = map(int, input().split())
def s(t, n): [print(*t)] if len(t) == M else [s(t + [i], i + 1) for i in range(n, N + 1)]
s([], 1)