import sys
input = sys.stdin.readline

N = int(input().rstrip())
before_max = list(map(int, input().rstrip().split()))
before_min = before_max[:]

for _ in range(1, N):
    current = list(map(int, input().rstrip().split()))
    current_max = [
        max(before_max[0], before_max[1]) + current[0],
        max(before_max[0], before_max[1], before_max[2]) + current[1],
        max(before_max[1], before_max[2]) + current[2]
    ]
    current_min = [
        min(before_min[0], before_min[1]) + current[0],
        min(before_min[0], before_min[1], before_min[2]) + current[1],
        min(before_min[1], before_min[2]) + current[2]
    ]
    before_max = current_max
    before_min = current_min

print(max(before_max), min(before_min))
