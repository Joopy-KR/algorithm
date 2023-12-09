import sys
input = sys.stdin.readline

N = int(input().rstrip())

checkpoint = []
distance = []

for _ in range(N):
    x, y = map(int, input().rstrip().split())

    checkpoint.append([x, y])

for i in range(N - 1):
    distance.append(abs(checkpoint[i + 1][0] - checkpoint[i][0]) + abs(checkpoint[i + 1][1] - checkpoint[i][1]))

total_distance = sum(distance)

min_result = sys.maxsize

for j in range(1, N - 1):
    # 자기 오는 길 빼주고 뒤에꺼랑 앞에꺼 거리로 다시 더해주면 됨
    dist = total_distance - (abs(checkpoint[j - 1][0] - checkpoint[j][0]) + abs(checkpoint[j - 1][1] - checkpoint[j][1])) - (abs(checkpoint[j + 1][0] - checkpoint[j][0]) + abs(checkpoint[j + 1][1] - checkpoint[j][1])) + (abs(checkpoint[j + 1][0] - checkpoint[j - 1][0]) + abs(checkpoint[j + 1][1] - checkpoint[j - 1][1]))

    min_result = min(min_result, dist)

print(min_result)