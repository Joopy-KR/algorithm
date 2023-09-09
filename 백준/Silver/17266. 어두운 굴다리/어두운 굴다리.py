import math

N = int(input())
M = int(input())
x = list(map(int, input().split()))

# 그냥 젤 먼거리 기준으로 잡아주면 되는거 아닌가?
max_val = 0
result = 0

for i in range(M):
    if i == 0:
        if x[i] > max_val:
            max_val = x[i]
            result = max_val
    else:
        if x[i] - x[i - 1] > max_val:
            max_val = x[i] - x[i - 1]
            temp = math.ceil(max_val / 2)
            if temp > result:
                result = temp

if N - x[-1] > max_val:
    max_val = N - x[-1]
    if max_val > result:
        result = max_val

print(result)

