import sys
input = sys.stdin.readline

N, K = map(int, input().split())

checkpoint = []
distance = []

if K == 0:
    for _ in range(N):
        x, y = map(int, input().rstrip().split())

        checkpoint.append([x, y])

    for i in range(N - 1):
        distance.append(abs(checkpoint[i + 1][0] - checkpoint[i][0]) + abs(checkpoint[i + 1][1] - checkpoint[i][1]))

    total_distance = sum(distance)

    print(total_distance)

elif K == 1:
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

else:
    INF = sys.maxsize 
    point = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    distance = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            distance[i][j] = abs(point[i][0] - point[j][0]) + abs(point[i][1] - point[j][1])

    dp = [[INF for _ in range(N)] for _ in range(K + 1)]
    dp[0][0] = 0

    for i in range(1, N):
        dp[0][i] = dp[0][i - 1] + distance[i - 1][i]

    for i in range(1, K + 1):
        dp[i][0], dp[i][1] = 0, dp[i - 1][1]
        dp[i][i] = distance[0][i]
        for j in range(1, N):
            for m in range(i, 0, -1):
                if j - m - 1 < 0:
                    continue
                dp[i][j] = min(dp[i][j], dp[i - m][j - m - 1] + distance[j][j - m - 1], dp[i][j - 1] + distance[j - 1][j])

    print(dp[-1][-1])
    