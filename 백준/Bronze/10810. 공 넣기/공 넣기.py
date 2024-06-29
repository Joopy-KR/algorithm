import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [0] * (N + 1)
for _ in range(M):
    i, j, k = map(int, input().rstrip().split())
    for idx in range(i, j + 1):
        arr[idx] = k

print(*arr[1:])
