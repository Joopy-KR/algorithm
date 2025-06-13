import sys
input = sys.stdin.readline
from copy import deepcopy

N = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
std_arr = deepcopy(arr)
for i in range(N):
    if i == N - 1:
        continue
    for j in range(len(arr[i])):
        if arr[i][j] + std_arr[i + 1][j] > arr[i + 1][j]:
            arr[i + 1][j] = arr[i][j] + std_arr[i + 1][j]
        if arr[i][j] + std_arr[i + 1][j + 1] > arr[i + 1][j + 1]:
            arr[i + 1][j + 1] = arr[i][j] + std_arr[i + 1][j + 1]

print(max(arr[N - 1]))