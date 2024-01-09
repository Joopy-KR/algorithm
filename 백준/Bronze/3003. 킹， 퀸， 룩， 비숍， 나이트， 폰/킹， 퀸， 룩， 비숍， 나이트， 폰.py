# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#

arr = list(map(int, input().split()))

check = [1, 1, 2, 2, 2, 8]

result = [0] * len(arr)

for i in range(6):
    if arr[i] - check[i] < 0:
        result[i] = abs(check[i] - arr[i])
    elif arr[i] - check[i] > 0:
        result[i] = -abs(check[i] - arr[i])

print(*result)