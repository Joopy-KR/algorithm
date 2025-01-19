import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
before_max = arr[0]
before_min = arr[0]
current_max = arr[0]
current_min = arr[0]

for i in range(1, N):
    current_max = [
        max(before_max[0], before_max[1]) + arr[i][0],
        max(before_max[0], before_max[1], before_max[2]) + arr[i][1],
        max(before_max[1], before_max[2]) + arr[i][2]
    ]
    current_min = [
        min(before_min[0] + arr[i][0], before_min[1] + arr[i][0]),
        min(before_min[0] + arr[i][1], before_min[1] + arr[i][1], before_min[2] + arr[i][1]),
        min(before_min[1] + arr[i][2], before_min[2] + arr[i][2])
    ]
    before_max = current_max
    before_min = current_min

print(max(current_max), min(current_min))
