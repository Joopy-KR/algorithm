"""
1. 전체 사각형 넓이를 구한 후
2. 왼쪽에서 가면서, 더 높은기둥을 만나면 가로 x (최고 높이 - 현재 높이)
3. 최고 높이에 도달했다면 왼쪽 여백 사각형 넓이 구하기
4. 오른쪽도 반복
5. 전체 넓이에서 왼쪽 사각형 총합 빼고 오른쪽 빼면 넓이
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = [[] * N for _ in range(N)]
for i in range(N):
    l, h = map(int, input().rstrip().split())  # L: 기둥 왼쪽면 위치, H: 높이
    arr[i] = [l, h]

# 기둥 정렬
arr.sort()

# 최고 높이 계산
max_height = 0
for j in arr:
    if j[1] > max_height:
        max_height = j[1]

# 밑변 길이 계산
base_length = (arr[-1][0] + 1) - (arr[0][0])

# 전체 사각형 넓이
total_size = base_length * max_height

# 왼쪽에서 올라가기
# 2. 왼쪽에서 가면서, 더 높은기둥을 만나면 가로 x (최고 높이 - 현재 높이)
is_left_done = False
start = 0
left_result = 0
while not is_left_done:
    now_height = arr[start][1]
    for k in range(start, len(arr)):
        # 가다가 더 큰 친구를 발견하면
        if arr[k][1] > now_height:
            # 거기까지의 사각형 넓이 구해서 결과에 더해주고(가로 길이 * (제일 높은 길이 - 현재 높이))
            left_result += (arr[k][0] - arr[start][0]) * (max_height - now_height)
            # 현재 시작점이랑 높이 높은걸로 바꿔주기
            start = k
            now_height = arr[k][1]
            break
        # 만약 현재 높이가 최고점이라면, break
        if now_height == max_height:
            is_left_done = True

# 오른쪽도 반복
is_right_done = False
start = len(arr) - 1
right_result = 0
while not is_right_done:
    now_height = arr[start][1]
    for l in range(start, -1, -1):
        if arr[l][1] > now_height:
            right_result += ((arr[start][0] + 1) - (arr[l][0] + 1)) * (max_height - now_height)
            start = l
            now_height = arr[l][1]
            break
        if now_height == max_height:
            is_right_done = True

# 5. 전체 넓이에서 왼쪽 사각형 총합 빼고 오른쪽 빼면 넓이
print(total_size - left_result - right_result)