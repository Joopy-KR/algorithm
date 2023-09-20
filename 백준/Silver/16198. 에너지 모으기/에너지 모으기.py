from copy import deepcopy
import sys
input = sys.stdin.readline

N = int(input().rstrip())
W = list(map(int, input().rstrip().split()))
arr = [i for i in range(1, N - 1)]
path = [0] * (N - 2)
perm = []
max_val = 0

def backtracking(cnt):
    if cnt == N - 2:
        temp = deepcopy(path)
        perm.append(temp)
        return
    for num in arr:
        if num in path:
            continue
        path[cnt] = num
        backtracking(cnt + 1)
        path[cnt] = 0

backtracking(0)

for per in perm:
    temp = 0
    lst = deepcopy(W)
    for p in per:
        temp += lst[p - 1] * lst[p + 1]
        lst.pop(p)
        for c in range(len(per)):
            if per[c] > p:
                per[c] -= 1
    if temp > max_val:
        max_val = temp

print(max_val)