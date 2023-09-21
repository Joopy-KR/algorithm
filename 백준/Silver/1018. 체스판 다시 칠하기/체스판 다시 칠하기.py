"""
1. BFS 배열만들고
2. 8 * 8 범위 내에서 나가지 않는다면 싹다 돌려본 후
    2-1. 8 * 8 정답표를 만들어놓고
    2-2. 정답표랑 매칭 시킨다음에
    2-3. 최소값을 최소값으로 치자
3. 최소값으로 칠할 수 있는 경우를 찾자.
"""
import sys
input = sys.stdin.readline

answer1 = [
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
]

answer2 = [
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
]

N, M = map(int, input().rstrip().split())

arr = [list(map(str, input().rstrip())) for _ in range(N)]

min_val = 10000
for r in range(N - 7):
    for c in range(M - 7):
        temp_1 = 0
        temp_2 = 0
        min_temp = 10000
        for r1 in range(8):
            for c1 in range(8):
                if arr[r + r1][c + c1] != answer1[r1][c1]:
                    temp_1 += 1
                if arr[r + r1][c + c1] != answer2[r1][c1]:
                    temp_2 += 1
        min_temp = min(temp_1, temp_2)
        min_val = min(min_val, min_temp)

print(min_val)